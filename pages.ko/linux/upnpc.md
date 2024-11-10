# upnpc

> UPnP 프로토콜을 통해 라우터의 포트 포워딩 규칙을 구성합니다.
> 더 많은 정보: <https://manned.org/upnpc>.

- 외부 TCP 포트 80을 로컬 머신의 포트 8080으로 포워딩:

`upnpc -a {{192.168.0.1}} 8080 80 tcp`

- 외부 TCP 포트 80에 대한 포트 리디렉션 삭제:

`upnpc -d 80 tcp`

- 네트워크의 UPnP 장치 정보 가져오기:

`upnpc -s`

- 기존 리디렉션 나열:

`upnpc -l`
