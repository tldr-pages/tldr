# tcpreplay

> `pcap` 파일에 저장된 네트워크 트래픽을 재생.
> 더 많은 정보: <https://tcpreplay.appneta.com/wiki/tcpreplay-man.html>.

- 사용 가능한 네트워크 인터페이스 목록 표시:

`tcpreplay --listnics`

- 지정한 인터페이스로 트래픽 재생:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{트래픽.pcap}}`

- 지정한 인터페이스로 트래픽을 재생하고 상세 정보를 `stdout`에 출력:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-v|--verbose]}} {{트래픽.pcap}}`

- 지정한 인터페이스로 가능한 한 빠르게 트래픽 재생:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-t|--topspeed]}} {{트래픽.pcap}}`

- 지정한 Mbps 속도로 인터페이스에 트래픽 재생:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-M|--mbps]}} {{10}} {{트래픽.pcap}}`

- 지정한 횟수만큼 인터페이스에 트래픽 반복 재생:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-l|--loop]}} {{횟수}} {{트래픽.pcap}}`
