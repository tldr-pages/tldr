# acme.sh

> 实现 ACME 客户端协议的 Shell 脚本，是 `certbot` 的替代方案。
> 另见 `acme.sh dns`。
> 更多信息：<https://github.com/acmesh-official/acme.sh>。

- 使用 webroot 模式签发证书：

`acme.sh --issue --domain {{example.com}} --webroot {{/path/to/webroot}}`

- 使用独立模式在端口 80 为多个域签发证书：

`acme.sh --issue --standalone --domain {{example.com}} --domain {{www.example.com}}`

- 使用独立 TLS 模式在端口 443 签发证书：

`acme.sh --issue --alpn --domain {{example.com}}`

- 使用有效的 Nginx 配置签发证书：

`acme.sh --issue --nginx --domain {{example.com}}`

- 使用有效的 Apache 配置签发证书：

`acme.sh --issue --apache --domain {{example.com}}`

- 使用自动 DNS API 模式签发通配符（*）证书：

`acme.sh --issue --dns {{dns_cf}} --domain {{*.example.com}}`

- 将证书文件安装到指定位置（对自动证书续期非常有用）：

`acme.sh --install-cert -d {{example.com}} --key-file {{/path/to/example.com.key}} --fullchain-file {{/path/to/example.com.cer}} --reloadcmd "{{systemctl force-reload nginx}}"`