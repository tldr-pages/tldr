# cfssl

> Cloudflare 的 PKI 和 TLS 工具包。
> 另见：`openssl`。
> 更多信息：<https://github.com/cloudflare/cfssl>。

- 显示主机的证书信息：

`cfssl certinfo -domain {{www.google.com}}`

- 从文件解码证书信息：

`cfssl certinfo -cert {{path/to/certificate.pem}}`

- 扫描主机以查找 SSL/TLS 问题：

`cfssl scan {{host1 host2 ...}}`

- 显示子命令的帮助：

`cfssl {{genkey|gencsr|certinfo|sign|gencrl|ocspdump|ocsprefresh|ocspsign|ocspserve|scan|bundle|crl|print-defaults|revoke|gencert|serve|version|selfsign|info}} -h`