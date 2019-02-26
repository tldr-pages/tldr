# gunicorn

> Python 的 WSGI http服务器.

- 运行python web应用程序:

`gunicorn {{导入路径:应用程序}}`

- 在localhost上监听8080端口:

`gunicorn --bind {{localhost}}:{{8080}} {{导入路径:应用程序}}`

- 启用实时自动加载:

`gunicorn --reload {{导入路径:应用程序}}`

- 使用4个工作进程处理请求:

`gunicorn --workers {{4}} {{导入路径:应用程序}}`

- 使用4个工作线程处理请求:

`gunicorn --threads {{4}} {{导入路径:应用程序}}`

- 通过https运行应用程序:

`gunicorn --certfile {{cert.pem}} --keyfile {{key.pem}} {{导入路径:应用程序}}`
