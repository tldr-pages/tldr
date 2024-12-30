# prettier

> 一个针对 JavaScript、JSON、CSS、YAML 等的意见化代码格式化工具。
> 更多信息：<https://prettier.io/>。

- 格式化一个文件并将结果打印到 `stdout`：

`prettier {{path/to/file}}`

- 检查特定文件是否已被格式化：

`prettier --check {{path/to/file}}`

- 使用特定的配置文件运行：

`prettier --config {{path/to/config_file}} {{path/to/file}}`

- 格式化一个文件或目录，替换原始文件：

`prettier --write {{path/to/file_or_directory}}`

- 递归格式化文件或目录，使用单引号且不带尾随逗号：

`prettier --single-quote --trailing-comma {{none}} --write {{path/to/file_or_directory}}`

- 递归格式化 JavaScript 和 TypeScript 文件，替换原始文件：

`prettier --write "**/*.{js,jsx,ts,tsx}"`