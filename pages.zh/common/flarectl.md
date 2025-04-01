# flarectl

> Cloudflare 官方命令行工具。
> 更多信息：<https://github.com/cloudflare/cloudflare-go/blob/master/cmd/flarectl/README.md>。

- 封禁特定 IP：

`flarectl firewall rules create --zone="{{example.com}}" --value="{{8.8.8.8}}" --mode="{{block}}" --notes="{{封禁恶意用户}}"`

- 添加 DNS 记录：

`flarectl dns create --zone="{{example.com}}" --name="{{app}}" --type="{{CNAME}}" --content="{{myapp.herokuapp.com}}" --proxy`

- 列出所有 Cloudflare IPv4/IPv6 范围：

`flarectl ips --ip-type {{ipv4|ipv6|all}}`

- 使用 `domains.txt` 文件中的域名自动创建多个新的 Cloudflare 区域：

`for domain in $(cat {{domains.txt}}); do flarectl zone info --zone=$domain; done`

- 列出所有防火墙规则：

`flarectl firewall rules list`