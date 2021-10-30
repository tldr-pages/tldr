# iverilog

> Preprocesses and compiles Verilog HDL (IEEE-1364) code, into executable programs for simulation.
> More information: <http://iverilog.icarus.com/>.

- Compile a source file into an executable:

`iverilog {{source.v}} -o {{executable}}`

- Also display all warnings:

`iverilog {{source.v}} -Wall -o {{executable}}`

- Compile and run explicitly using the VVP runtime:

`iverilog -o {{executable}} -tvvp {{source.v}}`

- Compile using Verilog library files from a different path:

`iverilog {{source.v}} -o {{executable}} -I{{path/to/library_directory}}`

- Preprocess Verilog code without compiling:

`iverilog -E {{source.v}}`
