# dtc

> The Device Tree Compiler, a tool for recompiling device trees between formats.
> More information: <https://github.com/dgibson/dtc>.

- Decompile a `.dtb` file into a readable `.dts` file:

`dtc -I dtb -O dts -o {{output_file.dts}} {{input_file.dtb}}`
