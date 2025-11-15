# node

> 服务器后端 JavaScript 平台（Node.js）。
> 更多信息：<https://nodejs.org>.

- 运行一个 JavaScript 文件：

`node {{路径/到/文件}}`

- 开始一个 REPL 交互式解释器：

`node`

- 执行指定的文件，当导入的文件发生变化时重启进程（需要 Node.js 18.11+ 版本）：

`node --watch {{路径/到/文件}}`

- 执行输入的 JavaScript 代码：

`node {{[-e|--eval]}} "{{代码}}"`

- 执行输入的 JavaScript 代码并显示结果，用于打印 node 的依赖版本：

`node {{[-p|--print]}} "process.versions"`

- 启动检查器并在程序源码解析完成后等待调试器连接：

`node --no-lazy --inspect-brk {{路径/到/文件}}`
