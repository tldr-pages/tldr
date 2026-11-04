# tailcat

> Tailscale의 데이터 플레인을 사용해, WireGuard로 암호화된 터널을 제공 (netcat과 비슷하지만 암호화된 통신 사용).
> 아래 예제에서, `addrblob`은 실행 중인 `tailcat` 서버가 출력하는 연결 토큰 (`tcom...`), 클라이언트가 해당 서버에 연결 시 사용함.
> 더 많은 정보: <https://github.com/tailscale/tailcat#usage>.

- 하나의 연결을 수락하고 데이터를 `stdout`으로 출력하는 서버 시작 (로컬 포트 없음; 클라이언트는 출력된 addrblob을 사용해 연결):

`tailcat`

- 지정한 로컬 TCP 포트 (예: 22/80/443에 존재하는 서비스)를 터널을 통해 클라이언트에 공개:

`tailcat --serve={{22,80,443}}`

- 이 호스트 네트워크를 통해 클라이언트의 트래픽을 라우팅하는 exit node 서버 시작:

`tailcat --serve=exit-node`

- 인증이 필요 없는 SSH 서버 시작 (Linux/macOS):

`tailcat --serve=no-auth-ssh`

- addrblob을 사용하여 서버의 지정한 포트에 연결하고, `stdin`으로 받은 데이터를 서버로 전송:

`cat {{경로/대상/파일}} | tailcat {{addrblob}} {{포트}}`

- 직접 연결 경로가 만들어질 때까지 기다리며, 서버 연결 상태를 확인:

`tailcat ping --until-direct {{addrblob}}`

- 원격 머신에 SSH로 연결 (서버가 22번 포트를 공개해야 함):

`tailcat ssh {{addrblob}}`

- 새로운 서버 키를 생성하고 해당 addrblob 출력:

`tailcat genkey --force`
