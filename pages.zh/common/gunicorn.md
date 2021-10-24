# gunicorn

> Python 的 WSGI http 服务器。
> 更多信息：<https://gunicorn.org/>.

- 运行 python web 应用程序：

`gunicorn {{导入路径：应用程序}}`

- 在 localhost 上监听 8080 端口：

`gunicorn --bind {{localhost}}:{{8080}} {{导入路径：应用程序}}`

- 启用实时自动加载：

`gunicorn --reload {{导入路径：应用程序}}`

- 使用 4 个工作进程处理请求：

`gunicorn --workers {{4}} {{导入路径：应用程序}}`

- 使用 4 个工作线程处理请求：

`gunicorn --threads {{4}} {{导入路径：应用程序}}`

- 通过 https 运行应用程序：

`gunicorn --certfile {{cert.pem}} --keyfile {{key.pem}} {{导入路径：应用程序}}`
