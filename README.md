# Verilog-TestBench-ACP-Agent

**Hardware-Aware Autonomous Coding Agent**

A specialized agent designed to generate high-quality Verilog/SystemVerilog RTL, testbenches, and UVM components. It integrates with editors via the Agent Client Protocol (ACP) to provide a seamless hardware design workflow.

## Key Features

- **RTL Generation**: Produces synthesizable Verilog modules.
- **Verification**: Generates self-checking testbenches and UVM components.
- **Simulation Integration**: Automatically compiles and runs simulations using Icarus Verilog.
- **Debugging**: Analyzes simulation logs and waveforms to propose fixes.
- **ACP Integration**: Works directly within your editor context.

## Prerequisites

- **Icarus Verilog**: For simulation (`iverilog`, `vvp`).
  - Windows: [Bleeding Edge Builds](https://bleyer.org/icarus/) (Ensure added to PATH)
- **GTKWave**: For waveform viewing.

## Usage

Interact with the agent using natural language requests:

- "Create a 4-bit ALU with add, sub, and, or operations."
- "Generate a testbench for `alu.v` and verify all opcodes."
- "Run simulation and fix any errors."

## License

MIT
