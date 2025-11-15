# doctl balance

> Digital Ocean 계정의 잔액을 표시.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/balance/>.

- 현재 컨텍스트와 관련된 계정의 잔액을 가져옴:

`doctl balance get`

- 액세스 토큰과 연결된 계정 잔액을 가져옴:

`doctl balance get --access-token {{액세스_토큰}}`

- 지정된 컨텍스트와 연결된 계정의 잔액을 가져옴:

`doctl balance get --context`
