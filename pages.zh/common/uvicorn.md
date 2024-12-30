# uvicorn

> Python ASGI HTTP 服务器，用于异步项目。
> 更多信息：<https://www.uvicorn.org/>.

- 运行 Python web 应用：

`uvicorn {{import.path:app_object}}`

- 在本地主机的 8080 端口监听：

`uvicorn --host {{localhost}} --port {{8080}} {{import.path:app_object}}`

- 开启实时重载：

`uvicorn --reload {{import.path:app_object}}`

- 使用 4 个工作进程处理请求：

`uvicorn --workers {{4}} {{import.path:app_object}}`

- 通过 HTTPS 运行应用：

`uvicorn --ssl-certfile {{cert.pem}} --ssl-keyfile {{key.pem}} {{import.path:app_object}}`