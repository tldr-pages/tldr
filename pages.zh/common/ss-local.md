# ss-local

> 运行一个作为 SOCKS5 代理的 Shadowsocks 客户端。
> 更多信息：<https://github.com/shadowsocks/shadowsocks-libev/blob/master/doc/ss-local.asciidoc>.

- 通过指定主机、服务器端口、本地端口、密码和加密方法运行 Shadowsocks 代理：

`ss-local -s {{host}} -p {{server_port}} -l {{local_port}} -k {{password}} -m {{encrypt_method}}`

- 通过指定配置文件运行 Shadowsocks 代理：

`ss-local -c {{path/to/config/file.json}}`

- 使用插件运行代理客户端：

`ss-local --plugin {{plugin_name}} --plugin-opts {{plugin_options}}`

- 启用 TCP 快速打开：

`ss-local --fast-open`
