"""Check the public bootstrap without reading possible key/secret payloads."""
import argparse
import json
import os
import re
from html.parser import HTMLParser
from pathlib import Path

FORBIDDEN_PARTS = {".godot", ".import", "profiles", "userdata", "user_data", "saves", "player_saves", "test-profiles", "keystores", "sdk", "jdk", "tools", "node_modules", ".gradle", "export_templates", "private-evidence"}
FORBIDDEN_SUFFIXES = {".jks", ".keystore", ".key", ".pem", ".p12", ".pfx", ".apk", ".aab", ".exe", ".dll", ".so", ".pck", ".wasm", ".zip", ".tpz", ".log", ".save", ".pyc"}
PRIVATE_VALUE = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |ENCRYPTED )?PRIVATE KEY-----|\b(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}|\bAKIA[A-Z0-9]{16}\b|https://(?:drive\.google\.com/(?:file/d/|open\?)|chatgpt\.com/backend-api/)|(?:C:|D:)\\(?:Users|Program Files)\\", re.I)

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.urls.append(value)

def check(root):
    root = root.resolve()
    policy = json.loads((root / "ci/source-policy.json").read_text("utf-8"))
    allowed = set(policy["allow"])
    files = []
    problems = []
    for base, directories, names in os.walk(root, followlinks=False):
        directories[:] = [d for d in directories if d != ".git"]
        for directory in directories:
            if (Path(base) / directory).is_symlink():
                problems.append("symlink directory: " + str((Path(base) / directory).relative_to(root)))
        for name in names:
            path = Path(base) / name
            relative = path.relative_to(root).as_posix()
            parts = {p.lower() for p in path.relative_to(root).parts}
            if path.is_symlink() or parts & FORBIDDEN_PARTS or path.suffix.lower() in FORBIDDEN_SUFFIXES or name.lower().startswith(".env") or name.lower() == "export_credentials.cfg":
                problems.append("forbidden path (contents not read): " + relative)
                continue
            if relative not in allowed:
                problems.append("unapproved path (contents not read): " + relative)
                continue
            files.append(path)
            if path.stat().st_size > policy["max_file_bytes"]:
                problems.append("file budget: " + relative)
                continue
            try:
                content = path.read_text("utf-8")
            except UnicodeError:
                problems.append("non-text bootstrap file: " + relative)
                continue
            if PRIVATE_VALUE.search(content):
                problems.append("private value pattern: " + relative)
            if path.suffix == ".json":
                json.loads(content)
    actual = {p.relative_to(root).as_posix() for p in files}
    for missing in sorted(allowed - actual):
        problems.append("missing bootstrap file: " + missing)
    total = sum(p.stat().st_size for p in files)
    if total > policy["max_total_bytes"]:
        problems.append("total budget exceeded")
    status = json.loads((root / "site/status.json").read_text("utf-8"))
    for key, expected in policy["required_status"].items():
        if status.get(key) != expected:
            problems.append("unreviewed status: " + key)
    html = (root / "site/index.html").read_text("utf-8")
    for marker in ["Code27", "Pending", "status preview", "code26"]:
        if marker not in html:
            problems.append("missing preview label: " + marker)
    links = Links()
    links.feed(html)
    for url in links.urls:
        if url.startswith(("https://", "#", "data:")):
            continue
        target = (root / "site" / url.split("#")[0].split("?")[0]).resolve()
        if not target.is_relative_to(root / "site") or not target.is_file():
            problems.append("invalid local preview link: " + url)
    print(json.dumps({"status": "FAIL" if problems else "PASS", "files": len(files), "bytes": total, "problems": problems}, indent=2))
    return 1 if problems else 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    raise SystemExit(check(parser.parse_args().root))
