import os

WORKSPACE_ROOT = os.getcwd()

def file_read(path: str):
    full = os.path.join(WORKSPACE_ROOT, path)
    with open(full, "r", encoding="utf-8") as f:
        return {"content": f.read()}