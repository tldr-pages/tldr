# babel

> 一个将代码从 JavaScript ES6/ES7 语法转换为 ES5 语法的转换器。
> 更多信息：<https://babeljs.io/>.

- 转换指定的输入文件并输出到 `stdout`：

`babel {{path/to/file}}`

- 转换指定的输入文件并输出到特定文件：

`babel {{path/to/input_file}} --out-file {{path/to/output_file}}`

- 每次输入文件更改时进行转换：

`babel {{path/to/input_file}} --watch`

- 转换整个目录中的文件：

`babel {{path/to/input_directory}}`

- 忽略目录中指定的以逗号分隔的文件：

`babel {{path/to/input_directory}} --ignore {{ignored_file1,ignored_file2,...}}`

- 转换并输出为压缩的 JavaScript：

`babel {{path/to/input_file}} --minified`

- 选择一组预设进行输出格式化：

`babel {{path/to/input_file}} --presets {{preset1,preset2,...}}`

- 显示帮助信息：

`babel --help`