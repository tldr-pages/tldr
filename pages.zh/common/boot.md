# boot

> Clojure 编程语言的构建工具。
> 更多信息：<https://github.com/boot-clj/boot>.

- 启动一个 REPL 会话，可以是项目内的或独立的：

`boot repl`

- 构建一个单一的 `uberjar` 文件：

`boot jar`

- 基于模板生成新项目的脚手架：

`boot --dependencies boot/new new --template {{template_name}} --name {{project_name}}`

- 为开发构建（如果使用 boot/new 模板）：

`boot dev`

- 为生产构建（如果使用 boot/new 模板）：

`boot prod`

- 显示特定任务的帮助信息：

`boot {{task}} --help`
