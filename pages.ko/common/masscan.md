# masscan

> 가능한 한 빠르게 스캔하기 위한 네트워크 스캐너.
> 권한 상승 상태에서 실행하는 것이 가장 좋습니다. Nmap 호환성을 확인하려면 `masscan --nmap`을 실행하세요.
> 더 많은 정보: <https://manned.org/masscan>.

- IP 또는 네트워크 서브넷에서 포트 80 스캔:

`masscan {{IP_주소|네트워크_프리픽스}} --ports {{80}}`

- 클래스 B 서브넷을 초당 100,000 패킷의 속도로 상위 100개 포트 스캔:

`masscan {{10.0.0.0/16}} --top-ports {{100}} --rate {{100000}}`

- 특정 제외 파일의 범위를 피하여 클래스 B 서브넷 스캔:

`masscan {{10.0.0.0/16}} --top-ports {{100}} --excludefile {{경로/대상/파일}}`

- 인터넷에서 포트 80 및 443에서 실행 중인 웹 서버 스캔:

`masscan {{0.0.0.0/0}} --ports {{80,443}} --rate {{10000000}}`

- 인터넷에서 UDP 포트 53에서 실행 중인 DNS 서버 스캔:

`masscan {{0.0.0.0/0}} --ports {{U:53}} --rate {{10000000}}`

- 특정 포트 범위를 인터넷에서 스캔하고 파일로 내보내기:

`masscan {{0.0.0.0/0}} --ports {{0-65535}} --output-format {{binary|grepable|json|list|xml}} --output-filename {{경로/대상/파일}}`

- 파일에서 바이너리 스캔 결과를 읽고 `stdout`으로 출력:

`masscan --readscan {{경로/대상/파일}}`
