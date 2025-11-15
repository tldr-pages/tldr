# cfssl

> Cloudflare의 PKI 및 TLS 툴킷.
> 참고: `openssl`.
> 더 많은 정보: <https://github.com/cloudflare/cfssl>.

- 호스트의 인증서 정보 표시:

`cfssl certinfo -domain {{www.google.com}}`

- 파일에서 인증서 정보를 디코딩:

`cfssl certinfo -cert {{경로/대상/인증서.pem}}`

- 호스트에서 SSL/TLS 문제를 검색:

`cfssl scan {{호스트1 호스트2 ...}}`

- 하위 명령에 대한 도움말 표시:

`cfssl {{genkey|gencsr|certinfo|sign|gencrl|ocspdump|ocsprefresh|ocspsign|ocspserve|scan|bundle|crl|print-defaults|revoke|gencert|serve|version|selfsign|info}} -h`
