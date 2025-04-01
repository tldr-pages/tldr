# dtc

> 设备树编译器，用于在不同格式之间重新编译设备树。
> 更多信息：<https://github.com/dgibson/dtc>.

- 将 `.dtb` 文件反编译为可读的 `.dts` 文件：

`dtc -I dtb -O dts -o {{path/to/output_file.dts}} {{path/to/input_file.dtb}}`
