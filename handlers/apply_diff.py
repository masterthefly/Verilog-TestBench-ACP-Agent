import os

WORKSPACE_ROOT = os.getcwd()

def apply_diff(diff: dict):
    for f in diff.get("files", []):
        full = os.path.join(WORKSPACE_ROOT, f["path"])
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fp:
            fp.write(f["updated"])
    return {"success": True}