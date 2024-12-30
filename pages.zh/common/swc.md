# swc

> 用Rust编写的JavaScript和TypeScript编译器。
> 更多信息：<https://swc.rs>。

- 转换指定的输入文件并输出到`stdout`：

`swc {{path/to/file}}`

- 每次输入文件更改时都进行转换：

`swc {{path/to/file}} --watch`

- 转换指定的输入文件并输出到特定文件：

`swc {{path/to/input_file}} --out-file {{path/to/output_file}}`

- 转换指定的输入目录并输出到特定目录：

`swc {{path/to/input_directory}} --out-dir {{path/to/output_directory}}`

- 使用特定配置文件转换指定的输入目录：

`swc {{path/to/input_directory}} --config-file {{path/to/.swcrc}}`

- 使用glob路径忽略指定目录中的文件：

`swc {{path/to/input_directory}} --ignore {{path/to/ignored_file1 path/to/ignored_file2 ...}}`