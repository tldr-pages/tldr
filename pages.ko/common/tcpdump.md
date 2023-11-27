# tcpdump

> 네트워크의 트래픽 덤프.
> 더 많은 정보: <https://www.tcpdump.org>.

- 사용 가능한 네트워크 인터페이스 나열:

`tcpdump -D`

- 특정 인터페이스의 트래픽 캡처:

`tcpdump -i {{eth0}}`

- 콘솔에서 콘텐츠(ASCII)를 표시하는 모든 TCP 트래픽을 캡처:

`tcpdump -A tcp`

- 호스트에서 들어오고 나가는 트래픽을 캡처:

`tcpdump host {{www.example.com}}`

- 특정 인터페이스, 소스, 목적지 및 목적지 포트에서 트래픽을 캡처:

`tcpdump -i {{eth0}} src {{192.168.1.1}} and dst {{192.168.1.2}} and dst port {{80}}`

- 네트워크 트래픽 캡처:

`tcpdump net {{192.168.1.0/24}}`

- 포트 22를 통한 트래픽을 제외한 모든 트래픽을 캡처하고 덤프 파일에 저장:

`tcpdump -w {{dumpfile.pcap}} port not {{22}}`

- 지정된 덤프 파일에서 읽기:

`tcpdump -r {{dumpfile.pcap}}`
