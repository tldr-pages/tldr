# hledger-web

> `hledger` 是一个功能强大且友好的纯文本会计应用程序，`hledger-web` 为其提供了一个 Web 界面和 API。
> 更多信息：<https://hledger.org/hledger-web.html>。

- 启动 Web 应用程序，如果可能的话，还会启动浏览器，仅用于本地查看和添加：

`hledger-web`

- 如上，但指定文件并允许编辑现有数据：

`hledger-web --file {{path/to/file.journal}} --allow edit`

- 仅启动 Web 应用程序，并接受指定主机和端口的传入连接：

`hledger-web --serve --host {{my.host.name}} --port 8000`

- 仅启动 Web 应用程序的 JSON API，并仅允许读取访问：

`hledger-web --serve-api --host {{my.host.name}} --allow view`

- 显示已知的当前市场价值转换后的金额，以基础货币表示：

`hledger-web --value now --infer-market-prices`

- 如有可能，以 Info 格式显示手册：

`hledger-web --info`

- 显示帮助信息：

`hledger-web --help`
