# reflex

> 监视目录并在某些文件发生变化时重新运行命令。
> 更多信息：<https://github.com/cespare/reflex>.

- 如果任何文件发生变化，则使用 `make` 重新构建：

`reflex make`

- 如果任何 `.go` 文件发生变化，则编译并运行 Go 应用程序：

`reflex --regex='{{\.go$}}' {{go run .}}`

- 忽略目录中的变化：

`reflex --inverse-regex='{{^dir/}}' {{command}}`

- 当 reflex 启动和文件变化时运行命令：

`reflex --start-service=true {{command}}`

- 在命令中替换发生变化的文件名：

`reflex -- echo {}`
