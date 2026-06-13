# ss-local

> Shadowsocks 클라이언트를 SOCKS5 프록시로 실행.
> 더 많은 정보: <https://github.com/shadowsocks/shadowsocks-libev/blob/master/doc/ss-local.asciidoc>.

- 호스트, 서버 포트, 로컬 포트, 비밀번호 및 암호화 방법을 지정하여 Shadowsocks 프록시 실행:

`ss-local -s {{호스트}} -p {{서버_포트}} -l {{로컬_포트}} -k {{비밀번호}} -m {{암호화_방법}}`

- 구성 파일을 지정하여 Shadowsocks 프록시 실행:

`ss-local -c {{경로/대상/설정/파일.json}}`

- 플러그인을 사용하여 프록시 클라이언트 실행:

`ss-local --plugin {{플러그인_이름}} --plugin-opts {{플러그인_옵션}}`

- TCP 패스트 오픈 활성화:

`ss-local --fast-open`
