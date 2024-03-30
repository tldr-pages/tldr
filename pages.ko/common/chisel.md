# chisel

> Chisel은 TCP 터널을 생성하는 도구.
> 클라이언트와 서버 모두 포함.
> 더 많은 정보: <https://github.com/jpillora/chisel>.

- chisel 서버 실행:

`chisel server`

- 특정 포트를 수신하는 chisel 서버 실행:

`chisel server -p {{서버_포트}}`

- 사용자 이름 및 암호 인증을 사용하여 연결을 보호하는 chisel 서버 실행:

`chisel server --auth {{사용자이름}}:{{비밀번호}}`

- chisel 서버에 연결하고 특정 포트를 원격 서버 와 포트에 터널링:

`chisel client {{서버_IP}}:{{서버_포트}} {{로컬_포트}}:{{원격_서버}}:{{원격_포트}}`

- chisel 서버에 연결하고 특정 호스트와 포트를 원격 서버 및 포트에 터널링:

`chisel client {{서버_IP}}:{{서버_포트}} {{로컬_호스트}}:{{로컬_포트}}:{{원격_서버}}:{{원격_포트}}`

- 사용자 이름 및 암호 인증을 사용하여 chisel 서버에 연결:

`chisel client --auth {{사용자이름}}:{{비밀번호}} {{서버_IP}}:{{서버_포트}} {{local_port}}:{{원격_서버}}:{{원격_포트}}`
