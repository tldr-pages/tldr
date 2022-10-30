# verilator

> Converts Verilog and SystemVerilog hardware description language (HDL) designs into a C++ or SystemC model that after compiling can be executed.
> More information: <https://veripool.org/guide/latest/>.

- Build the C project in the current directory:

`verilator --binary -j 0 -Wall {{source.v}}`

- Create C++ executable:

`verilator --cc --exe --build -j 0 -Wall {{source.cpp}} {{out.v}}`

- Perform linting over the code in the current directory:

`verilator --lint-only -Wall`

- Create XML to feed into other tools:

`verilator --xml-only -Wall`
