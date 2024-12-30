# apx 堆栈

> 在 `apx` 中管理堆栈。
> 注意：用户创建的堆栈配置存储在 `~/.local/share/apx/stacks`。
> 更多信息：<https://github.com/Vanilla-OS/apx>。

- 交互式创建新的堆栈配置：

`apx stacks new`

- 交互式更新堆栈配置：

`apx stacks update {{name}}`

- 列出所有可用的堆栈配置：

`apx stacks list`

- 删除指定的堆栈配置：

`apx stacks rm --name {{string}}`

- 导入堆栈配置：

`apx stacks import --input {{path/to/stack.yml}}`

- 导出堆栈配置（注意：输出标志是可选的，默认导出到当前工作目录）：

`apx stacks export --name {{string}} --output {{path/to/output_file}}`