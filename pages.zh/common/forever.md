# forever

> 服务器端 JavaScript 应用程序，确保 Node.js 应用程序无限运行（在退出后重启）。
> 更多信息：<https://github.com/foreversd/forever>。

- 永久运行一个文件（作为守护进程）：

`forever {{script}}`

- 列出正在运行的 "forever" 进程（以及 "forever" 进程的 ID 和其他详细信息）：

`forever list`

- 停止一个正在运行的 "forever" 进程：

`forever stop {{ID|pid|script}}`