# ss-local

> Run a Shadowsocks client as a SOCKS5 proxy.
> More information: <https://github.com/shadowsocks/shadowsocks-c/blob/master/doc/ss-local.md>.

- Run a Shadowsocks proxy by specifying the host, server port, local port, password, and encryption method:

`ss-local -s {{host}} -p {{server_port}} -l {{local port}} -k {{password}} -m {{encrypt_method}}`

- Run a Shadowsocks proxy by specifying the configuration file:

`ss-local -c {{path/to/config_file.json}}`

- Use a plugin to run the proxy client:

`ss-local --plugin {{plugin_name}} --plugin-opts {{plugin_options}}`

- Enable TCP fast open:

`ss-local --fast-open`
