# verilator

> Converts Verilog and SystemVerilog hardware description language (HDL) designs into a C++ or SystemC model that after compiling can be executed.
> More information: <https://veripool.org/ftp/verilator_doc.pdf>.

- Create a binary:

`verilator --binary -j 0 -Wall {{source.v}}`

- Create C++ executable:

`verilator --cc --exe --build -j 0 -Wall {{source.cpp}} {{out.v}}`

- Perform linting:

`verilator --lint-only -Wall`

- Create XML to feed into other tools:

`verilator --xml-only -Wall`
