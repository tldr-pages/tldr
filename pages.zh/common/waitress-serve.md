# waitress-serve

> 纯 Python 的 WSGI HTTP 服务器。
> 更多信息：<https://docs.pylonsproject.org/projects/waitress/en/latest/runner.html>.

- 运行一个 Python Web 应用程序：

`waitress-serve {{import.path:wsgi_func}}`

- 在本地主机的 8080 端口上监听：

`waitress-serve --listen={{localhost}}:{{8080}} {{import.path:wsgi_func}}`

- 在 Unix 套接字上启动 waitress：

`waitress-serve --unix-socket={{path/to/socket}} {{import.path:wsgi_func}}`

- 使用 4 个线程处理请求：

`waitress-serve --threads={{4}} {{import.path:wsgifunc}}`

- 调用返回 WSGI 对象的工厂方法：

`waitress-serve --call {{import.path.wsgi_factory}}`

- 使用 HTTPS URL 方案：

`waitress-serve --url-scheme={{https}} {{import.path:wsgi_func}}`