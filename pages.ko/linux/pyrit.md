# pyrit

> 계산 능력을 활용한 WPA/WPA2 크래킹 도구.
> 더 많은 정보: <https://manned.org/pyrit>.

- 시스템 크래킹 속도 표시:

`pyrit benchmark`

- 사용 가능한 코어 나열:

`pyrit list_cores`

- [e]SSID 설정:

`pyrit -e "{{ESSID}}" create_essid`

- 특정 패킷 캡처 파일 [r]읽고 분석:

`pyrit -r {{경로/대상/파일.cap|경로/대상/파일.pcap}} analyze`

- 현재 데이터베이스에 비밀번호 [i]가져오기:

`pyrit -i {{경로/대상/파일}} {{import_unique_passwords|unique_passwords|import_passwords}}`

- 데이터베이스에서 특정 파일로 비밀번호 [o]내보내기:

`pyrit -o {{경로/대상/파일}} export_passwords`

- Pired 마스터 키로 비밀번호 변환:

`pyrit batch`

- 캡처 파일 [r]읽고 비밀번호 크래킹:

`pyrit -r {{경로/대상/파일}} attack_db`
