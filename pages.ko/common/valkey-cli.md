# valkey-cli

> Valkey 서버에 연결.
> 더 많은 정보: <https://valkey.io/topics/cli/>.

- 로컬 서버에 연결:

`valkey-cli`

- 기본 포트 (6379)를 사용하여 원격 서버에 연결:

`valkey-cli -h {{호스트}}`

- 포트 번호를 지정하여 원격 서버에 연결:

`valkey-cli -h {{호스트}} -p {{포트}}`

- URI를 지정하여 원격 서버에 연결:

`valkey-cli -u {{uri}}`

- 비밀번호 지정:

`valkey-cli -a {{비밀번호}}`

- valkey 명령 실행:

`valkey-cli {{valkey_명령어}}`

- 로컬 클러스터에 연결:

`valkey-cli -c`
