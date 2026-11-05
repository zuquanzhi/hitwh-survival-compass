"""Check required files and simple local Markdown links without dependencies."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

root = Path(__file__).resolve().parent.parent
required = ["README.md", "SUMMARY.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "docs/start.md"]
errors = []
for name in required:
    if not (root / name).is_file():
        errors.append(f"Missing required file: {name}")
for file in root.rglob("*.md"):
    if ".git" in file.relative_to(root).parts:
        continue
    content = file.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)(?:\s+[^)]*)?\)", content):
        parts = urlsplit(target.strip("<>"))
        if parts.scheme or parts.netloc or not parts.path:
            continue
        dest = (file.parent / unquote(parts.path)).resolve()
        if not dest.is_relative_to(root) or not dest.exists():
            errors.append(f"{file.relative_to(root)}: missing or outside repository: {target}")
if errors:
    print("\n".join(errors))
    raise SystemExit(1)
print("Required files and simple local Markdown links and images OK (anchors and rendering not checked).")
