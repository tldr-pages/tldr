# ss-local

> Գործարկել Shadowsocks հաճախորդը որպես SOCKS5 վստահված անձ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/shadowsocks/shadowsocks-libev/blob/master/doc/ss-local.asciidoc>:.

- Գործարկեք Shadowsocks-ի վստահված անձը` նշելով հյուրընկալողը, սերվերի պորտը, տեղական պորտը, գաղտնաբառը և գաղտնագրման եղանակը.:

`ss-local -s {{host}} -p {{server_port}} -l {{local port}} -k {{password}} -m {{encrypt_method}}`

- Գործարկեք Shadowsocks վստահված անձը` նշելով կազմաձևման ֆայլը.:

`ss-local -c {{path/to/config_file.json}}`

- Օգտագործեք plugin՝ վստահված անձի հաճախորդը գործարկելու համար.:

`ss-local --plugin {{plugin_name}} --plugin-opts {{plugin_options}}`

- Միացնել TCP արագ բացումը.:

`ss-local --fast-open`
