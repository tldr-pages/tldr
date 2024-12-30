# acme.sh --dns

> 使用 DNS-01 挑战来颁发 TLS 证书。
> 更多信息：<https://github.com/acmesh-official/acme.sh/wiki>。

- 使用自动 DNS API 模式颁发证书：

`acme.sh --issue --dns {{gnd_gd}} --domain {{example.com}}`

- 使用自动 DNS API 模式颁发通配符证书（用星号表示）：

`acme.sh --issue --dns {{dns_namesilo}} --domain {{example.com}} --domain {{*.example.com}}`

- 使用 DNS 别名模式颁发证书：

`acme.sh --issue --dns {{dns_cf}} --domain {{example.com}} --challenge-alias {{alias-for-example-validation.com}}`

- 在指定自定义等待时间（以秒为单位）的情况下颁发证书，同时禁用在 DNS 记录添加后自动轮询 Cloudflare/Google DNS：

`acme.sh --issue --dns {{dns_namecheap}} --domain {{example.com}} --dnssleep {{300}}`

- 使用手动 DNS 模式颁发证书：

`acme.sh --issue --dns --domain {{example.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`