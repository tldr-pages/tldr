# swc

> 用 Rust 编写的 JavaScript 和 TypeScript 编译器。
> 更多信息：<https://swc.rs>。

- 转译指定的输入文件并将输出到 `stdout`：

`swc {{path/to/file}}`

- 每当输入文件更改时，转译输入文件：

`swc {{path/to/file}} --watch`

- 转译指定的输入文件并将输出到指定文件：

`swc {{path/to/input_file}} --out-file {{path/to/output_file}}`

- 转译指定的输入目录并将输出到指定目录：

`swc {{path/to/input_directory}} --out-dir {{path/to/output_directory}}`

- 使用指定的配置文件转译指定的输入目录：

`swc {{path/to/input_directory}} --config-file {{path/to/.swcrc}}`

- 忽略使用 glob 路径指定的目录中的文件：

`swc {{path/to/input_directory}} --ignore {{path/to/ignored_file1 path/to/ignored_file2 ...}}`
