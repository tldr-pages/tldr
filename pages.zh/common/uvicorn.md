# uvicorn

> Python 的 ASGI HTTP 服务器，适用于异步项目。
> 更多信息：<https://www.uvicorn.org/settings/>.

- 运行 Python Web 应用：

`uvicorn {{导入路径:应用对象}}`

- 在本地主机上监听端口 8080：

`uvicorn --host {{localhost}} --port {{8080}} {{导入路径:应用对象}}`

- 启用实时重新加载：

`uvicorn --reload {{导入路径:应用对象}}`

- 使用 4 个工作进程处理请求：

`uvicorn --workers {{4}} {{导入路径:应用对象}}`

- 通过 HTTPS 运行应用：

`uvicorn --ssl-certfile {{cert.pem}} --ssl-keyfile {{key.pem}} {{导入路径:应用对象}}`
