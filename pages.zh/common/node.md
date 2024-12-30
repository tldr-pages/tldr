# 节点

> 服务器端 JavaScript 平台 (Node.js)。
> 更多信息：<https://nodejs.org>。

- 运行 JavaScript 文件：

`node {{path/to/file}}`

- 启动 REPL（交互式命令行）：

`node`

- 执行指定文件，并在导入的文件更改时重新启动进程（需要 Node.js 版本 18.11 及以上）：

`node --watch {{path/to/file}}`

- 通过将代码作为参数传递来评估 JavaScript 代码：

`node -e "{{code}}"`

- 评估并打印结果，适用于打印 Node 的依赖版本：

`node -p "process.versions"`

- 激活调试器，暂停执行直到连接调试器，一旦源代码完全解析：

`node --no-lazy --inspect-brk {{path/to/file}}`