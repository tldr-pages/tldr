# acme.sh --dns

> 使用 DNS-01 挑战来签发 TLS 证书。
> 更多信息：<https://github.com/acmesh-official/acme.sh/wiki>.

- 使用自动 DNS API 模式签发证书：

`acme.sh --issue --dns {{gnd_gd}} --domain {{example.com}}`

- 使用自动 DNS API 模式签发通配符证书（用星号表示）：

`acme.sh --issue --dns {{dns_namesilo}} --domain {{example.com}} --domain {{*.example.com}}`

- 使用 DNS 别名模式签发证书：

`acme.sh --issue --dns {{dns_cf}} --domain {{example.com}} --challenge-alias {{alias-for-example-validation.com}}`

- 在添加 DNS 记录后，通过指定自定义的等待时间（秒），在禁用 Cloudflare / Google DNS 自动轮询的同时签发证书：

`acme.sh --issue --dns {{dns_namecheap}} --domain {{example.com}} --dnssleep {{300}}`

- 使用手动 DNS 模式签发证书：

`acme.sh --issue --dns --domain {{example.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`
