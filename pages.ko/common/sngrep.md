# sngrep

> 터미널에서 SIP 호출 메시지 흐름을 표시.
> 더 많은 정보: <https://manned.org/sngrep>.

- PCAP 파일에서 SIP 패킷 시각화:

`sngrep -I {{경로/대상/파일.pcap}}`

- PCAP 파일에서 RTP 패킷이 포함된 INVITE 패킷으로 시작하는 대화만 시각화:

`sngrep -crI {{경로/대상/파일.pcap}}`

- RTP 패킷이 포함된 INVITE 패킷으로 시작하는 대화만 실시간 인터페이스로 표시:

`sngrep -cr`

- 인터페이스 없이 패킷을 파일로만 캡처:

`sngrep -NO {{경로/대상/파일.pcap}}`
