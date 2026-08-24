# ping

> 네트워크 호스트에 ICMP ECHO_REQUEST 패킷을 전송.
> Unix 계열 시스템과 달리, Windows의 `ping`은 기본적으로 4개의 패킷만 전송.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/ping>.

- 호스트에 4번 ping 전송:

`ping {{호스트}}`

- 지정한 횟수만큰 호스트에 ping을 전송:

`ping -n {{count}} {{호스트}}`

- 호스트에 지속적으로 ping 전송 (`<Ctrl c>`로 중단할 때까지):

`ping -t {{호스트}}`

- 각 응답을 기다리는 타임아웃을 밀리초 단위로 설정:

`ping -w {{밀리초}} {{호스트}}`

- ping 패킷의 버퍼 크기를 바이트 단위로 설정:

`ping -l {{바이트}} {{호스트}}`

- 특정 소스 IP 주소를 사용하여 호스트에 ping 전송:

`ping -S {{소스_아이피}} {{호스트}}`

- 주소를 호스트 이름으로 확인:

`ping -a {{호스트}}`
