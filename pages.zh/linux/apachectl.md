# apachectl

> 控制 Apache HTTP 服务器。
> 更多信息：<https://manned.org/apachectl>。

- 启动服务器：

`sudo apachectl start`

- 重启服务器：

`sudo apachectl restart`

- 停止服务器：

`sudo apachectl stop`

- 测试配置文件的有效性：

`apachectl configtest`

- 检查服务器状态（需要 lynx 浏览器）：

`apachectl status`

- 重新加载配置而不断开连接：

`sudo apachectl graceful`

- 打印完整的 Apache 配置：

`apachectl -S`

- 显示帮助：

`apachectl -h`