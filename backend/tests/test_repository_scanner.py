import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from utils.repository_scanner import RepositoryScanner


scanner = RepositoryScanner()

context = scanner.scan(
    "C:/Projets/ai-memory-agent"
)


print(f"Found {len(context.files)} files")

print("\n===== FILES =====")

for file in context.files[:100]:
    print(file)


print("\n===== FILE CONTEXT =====")

for file in context.file_contexts[:10]:
    print(
        f"""
Path: {file.path}
Extension: {file.extension}
Size: {file.size} bytes
Lines: {file.lines}
"""
    )