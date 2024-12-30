# lebab

> 一个用于将代码转译为 ES6/ES7 的 JavaScript 现代化工具。
> 所有示例必须提供转换。
> 更多信息：<https://github.com/lebab/lebab>。

- 使用一个或多个以逗号分隔的转换进行转译：

`lebab --transform {{transformation1,transformation2,...}}`

- 将文件转译到 `stdout`：

`lebab {{path/to/input_file}}`

- 将文件转译到指定的输出文件：

`lebab {{path/to/input_file}} --out-file {{path/to/output_file}}`

- 在指定目录、模式或文件中就地替换所有 `.js` 文件：

`lebab --replace {{directory|glob|file}}`

- 显示帮助信息：

`lebab --help`