# ss-local

> 运行一个Shadowsocks客户端作为SOCKS5代理。
> 更多信息：<https://github.com/shadowsocks/shadowsocks-libev/blob/master/doc/ss-local.asciidoc>。

- 通过指定主机、服务器端口、本地端口、密码和加密方式来运行Shadowsocks代理：

`ss-local -s {{host}} -p {{server_port}} -l {{local port}} -k {{password}} -m {{encrypt_method}}`

- 通过指定配置文件来运行Shadowsocks代理：

`ss-local -c {{path/to/config/file.json}}`

- 使用插件来运行代理客户端：

`ss-local --plugin {{plugin_name}} --plugin-opts {{plugin_options}}`

- 启用TCP快速打开：

`ss-local --fast-open`