# Introduction
## What is gem5 and a bit of history
First, there is M5 which is a simulator created at University of Michigan.

> Two Views of M5
> 1. A framework for event-driven simulation
> 	- Events, objects etc.
> 2. A collection of predefined object models
> 	- CPUs, caches, busses etc.

At the same time, there is a tool call Gems, created at Wisconsin. Gems from 50,000 feet a **Ruby** a memory System Simulator.

They are combined together in 2011, which is todays Gem5. 

It's like:
Michigan m5 + Wisconsin Gems = gem 5.

>The gem 5 simulator is a modular platform for computer-system architecture research, encompassing system-level architecture as well as processor microarchitecture.

Gem5's goals:
- applicaiton
- runtime
- compiler
- kernel
- ISA
- Arch
- Devices

## Citations for gem5

https://doi.org/10.48550/arXiv.2007.03152


![[Pasted image 20250904145921.png]]

Highlighted block is where computer architecture simulation fits in.
## Why we need simulation
- Need a tool to evaluate systems that don't exist.
	- Performance, power, energy, etc
- Very costly to actually make the hardware
- Computer Systems are complex with many interdependent parts
	- not easy to be accurate without the full system
- Simulation can be parameterized
	- Design-space exploration
	- Sensitivity analysis

## Kinds of simulation
- Functional Simulation
	- Executes programs correctly. Usually no timing information.
	- Used to validate correctness of compilers, etc.
	- RISC-V Spike, QEMU, gem5 atomic mode.
- Instrumentation-based
	- Often binary translation. Runs on actual hardware with callbacks.
	- Like trace-based. Not flexible to new ISA. Some things opaque
	- PIN, NVBit
- Trace-based
	- Generate addresses/events and re-execute
	- Can be fast (no need to do functional simulation) Reuse traces
	- If execution depends on timing, this will not work.
- Execution-driven
	- Functional and timing simulation is combined
	- gem5 and many others
	- gem5 is "execute in execute" or "timing directed"
- Full System
	- Components modeled with enough fidelity to run mostly  unmodified apps
	- Often "Bare metal" simulation
	- Often means running in the OS in the simulator, not faking it

Cycle-level Simulation
- Models the system cycle-by-cycle
- Often "event-driven"
- Can be highly accurate
	- not the exact same cycle-by-cycle as the ASIC, but similar timing
- Easily parameterizeable
	- no need for a full hardware design
- Faster than cycle-accurate
	- can "cheat" and functionally emulate some things

## Gem5's software architecture
Gem 5 is made up of C++ and python code.
- C++ side (Gem5 has hundreds of models)
	- Cache models (parameter: size)
	- Core models (parameter: LSQ, stages, ROB)
	- DRAM models (parameter: tRAS, tCAS, tRCD)

gem5 architecture: SimObject AKA Model
Model are the C++ code in the `src/` folder
Parameters:
Python code in `src/`
In SimObject declaration file

Instance or Configuration

# Getting started with Gem5

The most common way to use gem5 is to download the source and build it yourself.

```git
git clone https://github.com/gem5/gem5
cd gem5
```
There are two main branches in the gem5 repository:
Stable: The default branch for gem5.
Develop: The branch in which new features, improvements, etc.

> It is strongly suggested to _not_ try to compile gem5 when running on a virtual machine.
> 
> When running with a VM on a laptop gem5 can take over an hour just to compile.

# Reference
1. [Getting Started with gem5](https://www.gem5.org/getting_started/)
