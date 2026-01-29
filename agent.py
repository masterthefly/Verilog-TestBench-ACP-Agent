from antigravity import ToolRegistry
from handlers.file_read import file_read
from handlers.file_write import file_write
from handlers.apply_diff import apply_diff
from handlers.run_simulation import run_simulation
from handlers.lint_verilog import lint_verilog
from handlers.waveform_extract import waveform_extract

registry = ToolRegistry()

registry.register("file_read", file_read)
registry.register("file_write", file_write)
registry.register("apply_diff", apply_diff)
registry.register("run_simulation", run_simulation)
registry.register("lint_verilog", lint_verilog)
registry.register("waveform_extract", waveform_extract)