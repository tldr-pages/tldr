# acme.sh

> 实现了 ACME 客户端协议的 shell 脚本，是 certbot 的替代品。
> 另见 `acme.sh dns`。
> 更多信息：<https://github.com/acmesh-official/acme.sh>.

- 使用网站根目录模式签发证书：

`acme.sh --issue --domain {{example.com}} --webroot {{/路径/到/网站根目录}}`

- 使用独立模式和 80 端口为多个域名签发证书：

`acme.sh --issue --standalone --domain {{example.com}} --domain {{www.example.com}}`

- 使用独立 TLS 模式和 443 端口签发证书：

`acme.sh --issue --alpn --domain {{example.com}}`

- 使用运行中的 Nginx 的配置来签发证书：

`acme.sh --issue --nginx --domain {{example.com}}`

- 使用运行中的 Apache 的配置来签发证书：

`acme.sh --issue --apache --domain {{example.com}}`

- 使用自动 DNS API 模式签发一个通配符（\*）证书：

`acme.sh --issue --dns {{dns_cf}} --domain {{*.example.com}}`

- 将证书文件安装到指定位置（对自动更新证书很有用）：

`acme.sh --install-cert -d {{example.com}} --key-file {{/路径/到/example.com.key}} --fullchain-file {{/路径/到/example.com.cer}} --reloadcmd {{"systemctl force-reload nginx"}}`
