# certbot

> 用于自动获取和续订 TLS 证书的 Let's Encrypt 代理。
> 是 `letsencrypt` 的继任者。
> 更多信息：<https://certbot.eff.org/docs/using.html>.

- 通过 webroot 验证获取新证书，但不自动安装：

`sudo certbot certonly --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}}`

- 通过 Nginx 验证获取新证书，并自动安装新证书：

`sudo certbot --nginx --domain {{subdomain.example.com}}`

- 通过 Apache 验证获取新证书，并自动安装新证书：

`sudo certbot --apache --domain {{subdomain.example.com}}`

- 续订所有 30 天内过期的 Let's Encrypt 证书（别忘了之后重启使用这些证书的服务器）：

`sudo certbot renew`

- 模拟获取新证书，但实际不会将任何新证书保存到磁盘：

`sudo certbot --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --dry-run`

- 获取一个不受信任的测试证书：

`sudo certbot --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --test-cert`
