# asnmap

> ASN 정보를 기반으로 조직의 네트워크 범위를 매핑하는 Go 기반 CLI 도구.
> 참고: 사용하려면 ProjectDiscovery Cloud Platform의 API 키가 필요.
> 더 많은 정보: <https://github.com/projectdiscovery/asnmap#usage>.

- ASN에 대한 CIDR 범위 조회:

`asnmap {{[-a|-asn]}} {{AS5650}} -silent`

- IP 주소에 대한 CIDR 범위 조회:

`asnmap {{[-i|-ip]}} {{100.19.12.21}} -silent`

- 도메인에 대한 CIDR 범위 조회:

`asnmap {{[-d|-domain]}} {{example.com}} -silent`

- 조직 이름으로 CIDR 범위 조회:

`asnmap -org {{GOOGLE}} -silent`

- 대상 목록 파일을 기반으로 CIDR 범위 조회:

`asnmap {{[-f|-file]}} {{경로/대상/타겟파일.txt}} -silent`

- JSON 형식으로 결과 출력:

`asnmap {{[-d|-domain]}} {{facebook.com}} {{[-j|-json]}} -silent`

- CSV 형식으로 결과 출력:

`asnmap {{[-a|-asn]}} {{AS394161}} {{[-c|-csv]}} -silent`

- asnmap 최신 버전으로 업데이트:

`asnmap {{[-up|-update]}}`
