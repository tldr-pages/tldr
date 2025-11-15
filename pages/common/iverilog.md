# iverilog

> Preprocesses and compiles Verilog HDL (IEEE-1364) code into executable programs for simulation.
> More information: <https://github.com/steveicarus/iverilog>.

- Compile a source file into an executable:

`iverilog {{path/to/source.v}} -o {{path/to/executable}}`

- Compile a source file into an executable while displaying all warnings:

`iverilog {{path/to/source.v}} -Wall -o {{path/to/executable}}`

- Compile and run explicitly using the VVP runtime:

`iverilog -o {{path/to/executable}} -tvvp {{path/to/source.v}}`

- Compile using Verilog library files from a different path:

`iverilog {{path/to/source.v}} -o {{path/to/executable}} -I{{path/to/library_directory}}`

- Preprocess Verilog code without compiling:

`iverilog -E {{path/to/source.v}}`
