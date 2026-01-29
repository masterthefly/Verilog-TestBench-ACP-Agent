import os
import subprocess

WORKSPACE_ROOT = os.getcwd()

def lint_verilog(path: str):
    full = os.path.join(WORKSPACE_ROOT, path)
    proc = subprocess.run(["verilator", "--lint-only", full], capture_output=True, text=True)
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr
    }