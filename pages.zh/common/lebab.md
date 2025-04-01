# lebab

> 一个用于将代码转换为 ES6/ES7 的 JavaScript 现代化工具。
> 所有示例都必须提供转换方法。
> 更多信息：<https://github.com/lebab/lebab>.

- 使用一个或多个以逗号分隔的转换：

`lebab --transform {{transformation1,transformation2,...}}`

- 将文件转换并输出到 `stdout`：

`lebab {{path/to/input_file}}`

- 将文件转换并输出到指定的目标文件：

`lebab {{path/to/input_file}} --out-file {{path/to/output_file}}`

- 替换指定目录、通配符或文件中的所有 `.js` 文件：

`lebab --replace {{directory|glob|file}}`

- 显示帮助：

`lebab --help`