# reflex

> 监视一个目录，当某些文件发生更改时重新运行命令。
> 更多信息请访问: <https://github.com/cespare/reflex>。

- 如果任何文件更改，则使用 `make` 重新构建：

`reflex make`

- 如果任何 `.go` 文件更改，则编译并运行 Go 应用程序：

`reflex --regex='{{\.go$}}' {{go run .}}`

- 在监视更改时忽略一个目录：

`reflex --inverse-regex='{{^dir/}}' {{command}}`

- 当 reflex 启动并在文件更改时重新启动时运行命令：

`reflex --start-service=true {{command}}`

- 在下面替换发生更改的文件名：

`reflex -- echo {}`