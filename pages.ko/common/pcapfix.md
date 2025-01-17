# pcapfix

> 손상되거나 손괴된 PCAP 및 PcapNG 파일 복구.
> 더 많은 정보: <https://f00l.de/pcapfix/>.

- PCAP/PCapNG 파일 복구 (참고: PCAP 파일의 경우 각 패킷의 처음 262144바이트만 스캔):

`pcapfix {{경로/대상/파일.pcapng}}`

- 전체 PCAP 파일 복구:

`pcapfix --deep-scan {{경로/대상/파일.pcap}}`

- PCAP/PcapNG 파일을 복구하고 복구된 파일을 지정된 위치에 저장:

`pcapfix --outfile {{경로/대상/복구된파일.pcap}} {{경로/대상/파일.pcap}}`

- 지정된 파일을 자동 인식 무시하고 PcapNG 파일로 처리:

`pcapfix --pcapng {{경로/대상/파일.pcapng}}`

- 파일을 복구하고 과정을 자세히 표시:

`pcapfix --verbose {{경로/대상/파일.pcap}}`
