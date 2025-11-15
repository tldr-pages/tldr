# netsh interface portproxy

> 다양한 네트워크 구성 요소의 상태를 구성하고 표시합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/networking/technologies/netsh/netsh-interface-portproxy>.

- 현재 포트 전달 설정 표시:

`netsh interface portproxy show all`

- IPv4 포트 전달 설정 (관리자 권한 콘솔에서 실행):

`netsh interface portproxy add v4tov4 listenaddress={{192.168.0.1}} listenport={{8080}} connectaddress={{10.0.0.1}} connectport={{80}}`

- IPv4 포트 전달 삭제 (관리자 권한 콘솔에서 실행):

`netsh interface portproxy delete v4tov4 listenaddress={{192.168.0.1}} listenport={{8080}}`

- 도움말 표시:

`netsh interface portproxy`
