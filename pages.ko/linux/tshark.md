# tshark

> 패킷 분석 도구, Wireshark의 CLI 버전.
> 더 많은 정보: <https://tshark.dev/#sitemap-in-tshark---help>.

- 로컬호스트에서 모든 것 모니터링:

`tshark`

- 특정 캡처 필터와 일치하는 패킷만 캡처:

`tshark -f '{{udp port 53}}'`

- 특정 출력 필터와 일치하는 패킷만 표시:

`tshark -Y '{{http.request.method == "GET"}}'`

- 특정 프로토콜(예: HTTP)로 TCP 포트 디코딩:

`tshark -d tcp.port=={{8888}},{{http}}`

- 캡처된 출력의 형식 지정:

`tshark -T {{json|text|ps|...}}`

- 출력할 특정 필드 선택:

`tshark -T {{fields|ek|json|pdml}} -e {{http.request.method}} -e {{ip.src}}`

- 캡처된 패킷을 [f]파일에 저장:

`tshark -w {{경로/대상/파일}}`

- [f]파일에서 패킷 분석:

`tshark -r {{경로/대상/파일.pcap}}`
