# verilator

> Converts Verilog and SystemVerilog hardware description language (HDL) designs into a C++ or SystemC model that after compiling can be executed.
> More information: <https://veripool.org/ftp/verilator_doc.pdf>.

Example Verilog file:

```bash
mkdir test_our
cd test_our
cat >our.v <<'EOF'
module our;
initial begin $display("Hello World"); $finish; end
endmodule
EOF
```

- Create a binary:

`verilator --binary -j 0 -Wall our.v`

- Create C++ executable:

`verilator --cc --exe --build -j 0 -Wall {{source.cpp}} {{out.v}}`

- Perform linting:

`verilator --lint-only -Wall`

- Create XML to feed into other tools:
`verilator --xml-only -Wall`
