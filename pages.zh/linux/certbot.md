# certbot

> Let's Encrypt 的代理，用于自动获取和续订 TLS 证书。
> 是 `letsencrypt` 的继任者。
> 更多信息：<https://certbot.eff.org/docs/using.html>。

- 通过 webroot 授权获取新证书，但不自动安装：

`sudo certbot certonly --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}}`

- 通过 nginx 授权获取新证书，并自动安装新证书：

`sudo certbot --nginx --domain {{subdomain.example.com}}`

- 通过 apache 授权获取新证书，并自动安装新证书：

`sudo certbot --apache --domain {{subdomain.example.com}}`

- 续订所有将在 30 天内到期的 Let's Encrypt 证书（之后不要忘记重启使用这些证书的任何服务器）：

`sudo certbot renew`

- 模拟获取新证书，但不实际将任何新证书保存到磁盘：

`sudo certbot --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --dry-run`

- 获取一个不受信任的测试证书：

`sudo certbot --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --test-cert`