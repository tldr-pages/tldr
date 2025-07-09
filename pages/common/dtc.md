# dtc

> The Device Tree Compiler, a tool for recompiling device trees between formats.
> More information: <https://github.com/dgibson/dtc>.

- Compile a device tree source `.dts` file into a binary device tree blob `.dtb` file:

`dtc -I dts -O dtb -o {{path/to/output_file.dtb}} {{path/to/input_file.dts}}`

- Compile a device tree source `.dts` file into a binary device tree blob overlay `.dtbo` file:

`dtc -@ -I dts -O dtb -o {{path/to/output_file.dtbo}} {{path/to/input_file.dts}}`

- Decompile a device tree blob `.dtb` file into a readable device tree source `.dts` file:

`dtc -I dtb -O dts -o {{path/to/output_file.dts}} {{path/to/input_file.dtb}}`

- Decompile the current device tree from the system into a readable device tree source `.dts` file:

`dtc -I fs -O dts /proc/device-tree`
