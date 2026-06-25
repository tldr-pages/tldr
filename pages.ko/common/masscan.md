# masscan

> 매우 빠른 네트워크 스캐너.
> 관리자 권한으로 실행 시 가장 잘 동작. Nmap 호환성 도움말은 `masscan --nmap`을 실행.
> 관련 항목: `hping3`, `naabu`, `nmap`, `rustscan`, `zmap`.
> 더 많은 정보: <https://manned.org/masscan>.

- 특정 IP 또는 네트워크 대역에서 80번 포트 스캔:

`masscan {{ip_주소|네트워크_접두사}} {{[-p|--ports]}} {{80}}`

- Class B 서브넷에서 상위 100개 포트를 초당 100,000 패킷 속도로 스캔:

`masscan {{10.0.0.0/16}} --top-ports {{100}} --rate {{100000}}`

- 제외 목록 파일에 지정된 주소 범위를 제외하고 Class B 서브넷 스캔:

`masscan {{10.0.0.0/16}} --top-ports {{100}} --excludefile {{경로/대상/파일}}`

- Nmap과 유사한 버전 탐지 (배너 수집) 사용해 Class B 서브넷 스캔:

`masscan {{10.0.0.0/16}} {{[-p|--ports]}} {{22,80}} --banners --rate {{100000}}`

- 인터넷 전체에서 80번 및 443벝 포트의 웹 서버 스캔:

`masscan {{0.0.0.0/0}} {{[-p|--ports]}} {{80,443}} --rate {{10000000}}`

- 인터넷 전체에서 UDP 53번 포트의 DNS 서버 스캔:

`masscan {{0.0.0.0/0}} {{[-p|--ports]}} {{U:53}} --rate {{10000000}}`

- 특정 포트 범위를 스캔하고 결과를 파일로 저장:

`masscan {{0.0.0.0/0}} {{[-p|--ports]}} {{0-65535}} --output-format {{binary|grepable|json|list|xml}} --output-filename {{경로/대상/파일}}`

- 바이너리 형식의 스캔 결과 파일을 읽어, 표준 출력(`stdout`)으로 표시:

`masscan --readscan {{경로/대상/파일}}`
