# ipaggcreate

> TCP/IP 덤프에서 집계 통계를 생성하는 도구.
> 더 많은 정보: <https://manned.org/ipaggcreate>.

- PCAP 파일에서 각 소스 주소별 전송 패킷 수 집계:

`ipaggcreate --src {{경로/대상/파일.pcap}}`

- 네트워크 인터페이스에서 읽은 패킷을 IP 패킷 길이 기준으로 그룹화 및 집계:

`ipaggcreate --interface {{eth0}} --length`

- PCAP 파일에서 주소 쌍 간 전송된 바이트 수 집계:

`ipaggcreate --address-pairs --bytes {{경로/대상/파일.pcap}}`
