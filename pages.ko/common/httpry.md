# httpry

> HTTP 트래픽을 표시하고 기록하기 위한 경량 패킷 스니퍼.
> 구문 분석되는 트래픽을 실시간으로 표시하거나 출력 파일에 기록하는 데몬 프로세스로 실행될 수 있음.
> 더 많은 정보: <https://dumpsterventures.com/jason/httpry/>.

- 출력을 파일로 저장:

`httpry -o {{경로/대상/파일.log}}`

- 특정 인터페이스를 수신하고 출력을 바이너리 PCAP 형식 파일로 저장:

`httpry {{eth0}} -b {{경로/대상/파일.pcap}}`

- 쉼표로 구분된 HTTP 동사 목록으로 출력을 필터링:

`httpry -m {{get|post|put|head|options|delete|trace|connect|patch}}`

- 입력 캡처 파일에서 IP로 필터링:

`httpry -r {{경로/대상/파일.log}} '{{host 192.168.5.25}}'`

- 데몬 프로세스로 실행:

`httpry -d -o {{경로/대상/파일.log}}`
