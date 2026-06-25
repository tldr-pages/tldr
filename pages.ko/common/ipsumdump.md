# ipsumdump

> TCP/IP 덤프를 사람, 기계가 읽을 수 있는 ASCII 포맷으로 요약해주는 도구.
> 더 많은 정보: <https://manned.org/ipsumdump>.

- PCAP 파일 내 모든 패킷에 대해 출발지/목적지 IP 출력:

`ipsumdump --src --dst {{경로/대상/파일.pcap}}`

- 네트워크 인터페이스에서 읽은 패킷의 타임스탬프, 출발지 및 목적지 주소와 포트, 프로토콜 출력:

`ipsumdump --interface {{eth0}} -tsSdDp`

- PCAP 파일의 모든 패킷에 대해 익명화된 출발지 및 목적지 IP와 패킷 길이 출력:

`ipsumdump --src --dst --length --anonymize {{경로/대상/파일.pcap}}`
