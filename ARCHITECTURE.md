# Architecture

## High-Level Workflow

The agent operates as an intelligent loop between the user, the codebase, and the simulation tools.

```mermaid
graph TD
    User[User / Editor] -->|Request| Agent[Verilog ACP Agent]
    Agent -->|Read/Write| Files[Verilog Files]
    Agent -->|Execute| Sim[Simulator (iverilog)]
    Sim -->|Logs/VCD| Agent
    Agent -->|Response/Diffs| User
```

## Simulation Loop

When a verification task is requested, the agent follows a strict analyze-simulate-debug cycle.

```mermaid
sequenceDiagram
    participant User
    participant Agent
    participant Simulator

    User->>Agent: "Verify module X"
    Agent->>Agent: Generate Plan & Testbench
    Agent->>Files: Write tb_X.v
    loop Debug Cycle
        Agent->>Simulator: Compile (iverilog)
        alt Compile Error
            Simulator-->>Agent: Error Logs
            Agent->>Files: Fix Syntax
        else Compile Success
            Agent->>Simulator: Run (vvp)
            Simulator-->>Agent: Simulation Logs / VCD
            Agent->>Agent: Analyze Results
            opt Verification Fail
                Agent->>Files: Fix Logic / Testbench
            end
        end
    end
    Agent->>User: Success Report
```
