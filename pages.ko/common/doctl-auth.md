# doctl auth

> API 토큰으로 `doctl`을 인증.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/auth/>.

- API 토큰을 입력하고 해당 컨텍스트에 라벨을 지정하라는 메시지를 열기:

`doctl auth init --context {{토큰_라벨}}`

- 인증 컨텍스트 나열 (API 토큰):

`doctl auth list`

- 컨텍스트 전환 (API 토큰):

`doctl auth switch --context {{토큰_라벨}}`

- 저장된 인증 컨텍스트 제거 (API 토큰):

`doctl auth remove --context {{토큰_라벨}}`

- 사용 가능한 명령 표시:

`doctl auth --help`
