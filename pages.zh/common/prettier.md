# prettier

> 一个具有明确意见的代码格式化工具，支持 JavaScript、JSON、CSS、YAML 等。
> 更多信息：<https://prettier.io/>.

- 格式化文件并将结果输出到 `stdout`：

`prettier {{path/to/file}}`

- 检查特定文件是否已格式化：

`prettier --check {{path/to/file}}`

- 使用特定的配置文件运行：

`prettier --config {{path/to/config_file}} {{path/to/file}}`

- 格式化文件或目录，替换原始内容：

`prettier --write {{path/to/file_or_directory}}`

- 使用单引号且不带尾随逗号递归格式化文件或目录：

`prettier --single-quote --trailing-comma {{none}} --write {{path/to/file_or_directory}}`

- 递归格式化 JavaScript 和 TypeScript 文件，替换原始内容：

`prettier --write "**/*.{js,jsx,ts,tsx}"`