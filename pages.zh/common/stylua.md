# stylua

> 一个有观点的 Lua 代码格式化工具。
> 更多信息：<https://github.com/JohnnyMorganz/StyLua>。

- 自动格式化一个文件或整个目录：

`stylua {{path/to/file_or_directory}}`

- 检查特定文件是否已被格式化：

`stylua --check {{path/to/file}}`

- 使用特定配置文件运行：

`stylua --config-path {{path/to/config_file}} {{path/to/file}}`

- 从 `stdin` 格式化代码并输出到 `stdout`：

`stylua - < {{path/to/file.lua}}`

- 使用空格格式化文件或目录，并优先使用单引号：

`stylua --indent-type {{Spaces}} --quote-style {{AutoPreferSingle}} {{path/to/file_or_directory}}`