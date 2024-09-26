# dtc

> Device Tree Compiler
> A tool for recompiling device trees between formats.
> See <https://github.com/dgibson/dtc>

-- Decompile a dtb file into a readable dts file:

`dtc -I dtb -O dts -o {{output_file.dts}} {{input_file.dtb}}`
