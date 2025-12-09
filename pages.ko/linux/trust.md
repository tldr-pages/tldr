# trust

> 신뢰 정책 저장소를 운영합니다.
> 더 많은 정보: <https://manned.org/trust>.

- 신뢰 정책 저장소 항목 나열:

`trust list`

- 신뢰 정책 저장소의 특정 항목에 대한 정보 나열:

`trust list --filter={{blocklist|ca-anchors|certificates|trust-policy}}`

- 특정 신뢰 앵커를 신뢰 정책 저장소에 저장:

`trust anchor {{경로/대상/인증서.crt}}`

- 특정 앵커를 신뢰 정책 저장소에서 제거:

`trust anchor --remove {{경로/대상/인증서.crt}}`

- 공유 신뢰 정책 저장소에서 신뢰 정책 추출:

`trust extract --format=x509-directory --filter=ca-anchors {{경로/대상/폴더}}`

- 하위 명령에 대한 도움말 표시:

`trust {{하위_명령}} --help`
