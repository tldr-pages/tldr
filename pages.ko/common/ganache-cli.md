# ganache-cli

> 이더리움 개발을 위한 개인 블록체인 Ganache의 명령줄 버전.
> 더 많은 정보: <https://www.trufflesuite.com/ganache>.

- Ganache 실행:

`ganache-cli`

- 특정 수의 계정으로 Ganache를 실행:

`ganache-cli --accounts={{계정_의_수}}`

- Ganache를 실행하고 기본적으로 사용 가능한 계정을 잠금:

`ganache-cli --secure`

- Ganache 서버를 실행하고 특정 계정을 잠금 해제:

`ganache-cli --secure --unlock "{{계정_개인_키1}}" --unlock "{{계정_개인_키2}}"`

- 특정 계정과 잔액으로 Ganache을 실행:

`ganache-cli --account="{{계정_개인_키}},{{계정_잔액}}"`

- 기본 잔액이 있는 계정으로 Ganache를 실행:

`ganache-cli --defaultBalanceEther={{기본_잔액}}`

- Ganache를 실행하고 모든 요청을 `stdout`에 기록:

`ganache-cli --verbose`
