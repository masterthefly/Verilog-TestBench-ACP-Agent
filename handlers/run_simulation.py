import os
import subprocess

WORKSPACE_ROOT = os.getcwd()

def run_simulation(top_module, testbench_path, source_files=None, defines=None, flags=None):
    source_files = source_files or []
    defines = defines or []
    flags = flags or []

    tb_full = os.path.join(WORKSPACE_ROOT, testbench_path)
    src_full = [os.path.join(WORKSPACE_ROOT, s) for s in source_files]

    # Use absolute paths for Windows environment
    iverilog_bin = r"C:\iverilog\bin\iverilog.exe"
    vvp_bin = r"C:\iverilog\bin\vvp.exe"

    build_cmd = [iverilog_bin, "-o", "sim.out", tb_full] + src_full + defines + flags
    build = subprocess.run(build_cmd, capture_output=True, text=True)

    if build.returncode != 0:
        return {
            "phase": "compile",
            "exit_code": build.returncode,
            "stdout": build.stdout,
            "stderr": build.stderr,
            "vcd_path": None
        }

    run = subprocess.run([vvp_bin, "sim.out"], capture_output=True, text=True)

    vcd_path = None
    if os.path.exists("dump.vcd"):
        vcd_path = "dump.vcd"

    return {
        "phase": "run",
        "exit_code": run.returncode,
        "stdout": run.stdout,
        "stderr": run.stderr,
        "vcd_path": vcd_path
    }