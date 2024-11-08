# resolvectl

> 도메인 이름, IPv4 및 IPv6 주소, DNS 리소스 레코드 및 서비스를 해석.
> DNS 해석기를 검사하고 재구성.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/resolvectl.html>.

- DNS 설정 표시:

`resolvectl status`

- 하나 이상의 도메인에 대한 IPv4 및 IPv6 주소 해석:

`resolvectl query {{도메인1 도메인2 ...}}`

- 지정한 IP 주소의 도메인 검색:

`resolvectl query {{IP_주소}}`

- 모든 로컬 DNS 캐시 플러시:

`resolvectl flush-caches`

- DNS 통계(트랜잭션, 캐시 및 DNSSEC 판결) 표시:

`resolvectl statistics`

- 도메인의 MX 레코드 검색:

`resolvectl --legend={{no}} --type={{MX}} query {{도메인}}`

- 예를 들어 _xmpp-server._tcp gmail.com와 같은 SRV 레코드 해석:

`resolvectl service _{{서비스}}._{{프로토콜}} {{이름}}`

- TLS 키 검색:

`resolvectl tlsa tcp {{도메인}}:443`
