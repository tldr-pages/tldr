# hledger-web

> `hledger` 的网页界面和 API，一个强大、友好的纯文本会计应用程序。
> 更多信息：<https://hledger.org/hledger-web.html>。

- 启动网页应用程序，并在可能的情况下启动浏览器，以便本地查看和仅添加数据：

`hledger-web`

- 如上所述，但指定文件，并允许编辑现有数据：

`hledger-web --file {{path/to/file.journal}} --allow edit`

- 仅启动网页应用程序，并接受到指定主机和端口的传入连接：

`hledger-web --serve --host {{my.host.name}} --port 8000`

- 仅启动网页应用程序的 JSON API，并仅允许读取访问：

`hledger-web --serve-api --host {{my.host.name}} --allow view`

- 当已知时，以您的基础货币显示转换为当前市场价值的金额：

`hledger-web --value now --infer-market-prices`

- 如果可能，以信息格式显示手册：

`hledger-web --info`

- 显示帮助：

`hledger-web --help`