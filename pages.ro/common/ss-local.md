# ss-local

> Executați un client Shadowsocks ca proxy SOCKS5.
> Mai multe informaţii: <https://github.com/shadowsocks/shadowsocks-libev/blob/master/doc/ss-local.asciidoc>

- Rulați un proxy Shadowsocks specificând gazdă, portul server, portul local, parola și metoda de criptare:

`ss-local -s {{host}} -p {{server_port}} -l {{local port}} -k {{password}} -m {{encrypt_method}}`

- Rulați un proxy Shadowsocks specificând fișierul de configurare:

`ss-local -c {{path/to/config/file.json}}`

- Utilizați un plugin pentru a rula clientul proxy:

`ss-local --plugin {{plugin_name}} --plugin-opts {{plugin_options}}`

- Activați TCP deschis rapid:

`ss-local --fast-open`
