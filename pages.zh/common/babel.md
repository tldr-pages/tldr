# babel

> 一款JavaScript的编译器，将下一代ES语法转换为兼容语法。
> 详见: <https://babeljs.io/>.

- 转编译指定文件到标准输出:

`babel {{path/to/file}}`

- 转编译指定文件，输入为特定文件:

`babel {{path/to/input_file}} --out-file {{path/to/output_file}}`

- 监听文件变动触发转编译:

`babel {{path/to/input_file}} --watch`

- 转编译整个目录下的js文件:

`babel {{path/to/input_directory}}`

- 跳过指定目录下指定文件的编译（多文件使用逗号---‘,’分割）:

`babel {{path/to/input_directory}} --ignore {{ignored_files}}`

- 转编译后，执行压缩:

`babel {{path/to/input_file}} --minified`

- 使用预设值:

`babel {{path/to/input_file}} --presets {{presets}}`
