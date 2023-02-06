# ss-local

> Futtasson egy Shadowsocks klienst SOCKS5 proxyként. További információ: <https://github.com/shadowsocks/shadowsocks-libev/blob/master/doc/ss-local.asciidoc>.

- A Shadowsocks proxy futtatása a hoszt, a kiszolgáló portja, a helyi port, a jelszó és a titkosítási módszer megadásával:

`ss-local -s {{host}} -p {{server_port}} -l {{local port}} -k {{password}} -m {{encrypt_method}}`

- Shadowsocks proxy futtatása a konfigurációs fájl megadásával:

`ss-local -c {{path/to/config/file.json}}`

- A proxy-kliens futtatásához egy bővítményt használjon:

`ss-local --plugin {{plugin_name}} --plugin-opts {{plugin_options}}`

- A TCP gyors megnyitásának engedélyezése:

`ss-local --fast-open`
