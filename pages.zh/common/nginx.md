# nginx

> Nginx Web 服务器。
> 更多信息：<https://nginx.org/en/>。

- 使用默认配置文件启动服务器：

`nginx`

- 使用自定义配置文件启动服务器：

`nginx -c {{configuration_file}}`

- 使用配置文件中所有相对路径的前缀启动服务器：

`nginx -c {{configuration_file}} -p {{prefix/for/relative/paths}}`

- 不影响正在运行的服务器的情况下测试配置：

`nginx -t`

- 通过发送信号重新加载配置，不会导致停机：

`nginx -s reload`
