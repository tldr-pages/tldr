# acme.sh --dns

> TLS 인증서를 발급하려면 DNS-01 챌린지를 사용.
> 더 많은 정보: <https://github.com/acmesh-official/acme.sh/wiki>.

- 자동 DNS API 모드를 사용해 인증서 발급:

`acme.sh --issue --dns {{gnd_gd}} --domain {{example.com}}`

- 자동 DNS API 모드를 사용하여 와일드카드 인증서 (별표로 표시) 발급:

`acme.sh --issue --dns {{dns_namesilo}} --domain {{example.com}} --domain {{*.example.com}}`

- DNS 별칭 모드를 사용해 인증서 발급:

`acme.sh --issue --dns {{dns_cf}} --domain {{example.com}} --challenge-alias {{alias-for-example-validation.com}}`

- 사용자 지정 대기 시간(초)을 지정해, DNS 레코드가 추가된 후 자동 Cloudflare 또는 Google DNS 폴링을 비활성화하는 동안 인증서를 발급:

`acme.sh --issue --dns {{dns_namecheap}} --domain {{example.com}} --dnssleep {{300}}`

- 수동 DNS 모드를 사용하여 인증서 발급:

`acme.sh --issue --dns --domain {{example.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`
