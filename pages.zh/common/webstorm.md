# webstorm

> JetBrains JavaScript 集成开发环境。
> 更多信息：<https://www.jetbrains.com/help/webstorm/working-with-the-ide-features-from-command-line.html>.

- 在 WebStorm 中打开当前目录：

`webstorm`

- 在 WebStorm 中打开特定目录：

`webstorm {{path/to/directory}}`

- 在 LightEdit 模式下打开特定文件：

`webstorm -e {{path/to/file1 path/to/file2 ...}}`

- 在 LightEdit 模式下打开并等待编辑完成特定文件：

`webstorm --wait -e {{path/to/file}}`

- 打开文件并将光标定位到特定行：

`webstorm --line {{line_number}} {{path/to/file}}`

- 打开并比较文件（支持最多 3 个文件）：

`webstorm diff {{path/to/file1 path/to/file2 path/to/optional_file3}}`

- 打开并执行三方合并：

`webstorm merge {{path/to/left_file}} {{path/to/right_file}} {{path/to/target_file}}`