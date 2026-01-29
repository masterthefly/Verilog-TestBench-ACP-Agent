import os

WORKSPACE_ROOT = os.getcwd()

def file_write(path: str, content: str):
    full = os.path.join(WORKSPACE_ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return {"success": True}