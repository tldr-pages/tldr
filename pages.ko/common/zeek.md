# zeek

> 패시브 네트워크 트래픽 분석기.
> 출력 및 로그 파일은 현재 작업 디렉토리에 저장됩니다.
> 더 많은 정보: <https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility>.

- 네트워크 인터페이스에서 실시간 트래픽 분석:

`sudo zeek --iface {{인터페이스}}`

- 네트워크 인터페이스에서 실시간 트래픽 분석 및 사용자 지정 스크립트 로드:

`sudo zeek --iface {{인터페이스}} {{스크립트1}} {{스크립트2}}`

- 네트워크 인터페이스에서 실시간 트래픽 분석, 스크립트 로드 없이:

`sudo zeek --bare-mode --iface {{인터페이스}}`

- 네트워크 인터페이스에서 `tcpdump` 필터를 적용하여 실시간 트래픽 분석:

`sudo zeek --filter {{경로/대상/필터}} --iface {{인터페이스}}`

- 네트워크 인터페이스에서 워치독 타이머를 사용하여 실시간 트래픽 분석:

`sudo zeek --watchdog --iface {{인터페이스}}`

- PCAP 파일에서 트래픽 분석:

`zeek --readfile {{경로/대상/파일.trace}}`
