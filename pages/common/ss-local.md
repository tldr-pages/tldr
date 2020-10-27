# ss-local

> Run a Shadowsocks client as a SOCKS5 proxy.
> More information: <https://github.com/shadowsocks/shadowsocks-libev/blob/master/doc/ss-local.asciidoc>.

- Run Shadowsocks proxy by specifying host, server port, local port, password, and encrypt method:

`ss-local -s {{host}} -p {{server_port}} -l {{local port}} -k {{password}} -m {{encrypt_method}}`

- Run Shadowsocks proxy by specifying the config file:

`ss-local -c {{path/to/config/file.json}}`

- Use plugin to run the proxy client:

`ss-local --plugin {{plugin_name}} --plugin-opts {{plugin_options}}`

- Enable TCP fast open:

`ss-local --fast-open`
