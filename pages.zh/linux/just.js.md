# just

> 一个适用于 Linux 的 V8 JavaScript 运行时。
> 更多信息：<https://github.com/just-js/just>。

- 启动一个交互式 Shell (REPL)：

`just`

- 运行一个 JavaScript 文件：

`just {{path/to/file.js}}`

- 通过传递参数来评估 JavaScript 代码：

`just eval "{{code}}"`

- 在同名目录中初始化一个新项目：

`just init {{project_name}}`

- 将 JavaScript 应用程序构建为可执行文件：

`just build {{path/to/file.js}} --static`
