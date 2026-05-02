# ipscan

> 간편하게 사용할 수 있는 빠른 네트워크 스캐너.
> Angry IP Scanner라고도 불림.
> 더 많은 정보: <https://www.aldeid.com/wiki/Angry-IPScan#CLI>.

- 특정 IP 주소 스캔:

`ipscan {{192.168.0.1}}`

- IP 주소 범위 스캔:

`ipscan {{192.168.0.1-254}}`

- IP 주소 범위를 스캔하고 결과를 파일로 저장:

`ipscan {{192.168.0.1-254}} -o {{경로/대상/출력파일.txt}}`

- 특정 포트 집합으로 IP를 스캔:

`ipscan {{192.168.0.1-254}} -p {{80,443,22}}`

- Scan with a delay between requests to avoid network congestion:

`ipscan {{192.168.0.1-254}} -d {{200}}`

- 도움말 표시:

`ipscan --help`
