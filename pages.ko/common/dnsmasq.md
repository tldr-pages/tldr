# dnsmasq

> 경량 DNS, DHCP, TFTP, PXE 서버.
> 더 많은 정보: <https://manned.org/dnsmasq>.

- 기본 설정으로 dnsmasq 시작:

`dnsmasq`

- 포그라운드에서 dnsmasq 실행 (디버깅용):

`dnsmasq --no-daemon`

- 사용자 정의 설정 파일 지정:

`dnsmasq --conf-file={{경로/대상/설정파일.conf}}`

- 상세 로그 출력 활성화:

`dnsmasq --log-queries --log-facility=-`

- DHCP 범위 및 임대 시간 설정:

`dnsmasq --dhcp-range={{192.168.0.50,192.168.0.150,12h}}`

- 버전 정보 표시:

`dnsmasq --version`

