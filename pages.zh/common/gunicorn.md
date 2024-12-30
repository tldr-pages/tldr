# gunicorn

> Python WSGI HTTP 服务器。
> 更多信息: <https://gunicorn.org/>.

- 运行 Python 网络应用：

`gunicorn {{import.path:app_object}}`

- 在本地主机的 8080 端口上监听：

`gunicorn --bind {{localhost}}:{{8080}} {{import.path:app_object}}`

- 开启实时重载：

`gunicorn --reload {{import.path:app_object}}`

- 使用 4 个工作进程处理请求：

`gunicorn --workers {{4}} {{import.path:app_object}}`

- 使用 4 个工作线程处理请求：

`gunicorn --threads {{4}} {{import.path:app_object}}`

- 通过 HTTPS 运行应用：

`gunicorn --certfile {{cert.pem}} --keyfile {{key.pem}} {{import.path:app_object}}`