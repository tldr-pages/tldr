# naabu

> 신뢰성과 단순성에 중점을 둔 Go로 작성된 빠른 포트 스캐너.
> 참고: 일부 기능은 `naabu`를 루트 권한으로 실행할 때만 활성화되며, 예를 들어 SYN 스캔이 있습니다.
> 더 많은 정보: <https://docs.projectdiscovery.io/tools/naabu/running>.

- 원격 호스트의 기본(상위 100개) 포트에 대해 SYN 스캔 실행:

`sudo naabu -host {{호스트}}`

- 사용 가능한 네트워크 인터페이스와 로컬 호스트의 공용 IP 주소 표시:

`naabu -interface-list`

- 원격 호스트의 모든 포트 스캔 (CONNECT 스캔, `sudo` 없이):

`naabu -p - -host {{호스트}}`

- 원격 호스트의 상위 1000개 포트 스캔:

`naabu -top-ports 1000 -host {{호스트}}`

- 원격 호스트의 TCP 포트 80, 443 및 UDP 포트 53 스캔:

`naabu -p 80,443,u:53 -host {{호스트}}`

- 원격 호스트가 사용하는 CDN 유형 표시 (있는 경우):

`naabu -p 80,443 -cdn -host {{호스트}}`

- 추가 기능을 위해 `naabu`에서 `nmap` 실행 (`nmap`이 설치되어 있어야 함):

`sudo naabu -v -host {{호스트}} -nmap-cli 'nmap {{-v -T5 -sC}}'`
