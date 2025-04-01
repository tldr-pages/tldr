# forever

> 服务器端 JavaScript 应用程序，确保 Node.js 应用程序无限期运行（退出后会自动重启）。
> 更多信息： <https://github.com/foreversd/forever>.

- 以守护进程方式启动并持续运行一个文件：

`forever {{script}}`

- 列出所有正在运行的 "forever" 进程（包括 ID 和其他 "forever" 进程的详细信息）：

`forever list`

- 停止一个正在运行的 "forever" 进程：

`forever stop {{ID|pid|script}}`
