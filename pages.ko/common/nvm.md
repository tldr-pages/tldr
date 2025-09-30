# nvm

> Node.js 버전을 설치, 제거 또는 전환.
> "12.8" 또는 "v16.13.1" 같은 버전 번호와 "stable", "system" 같은 레이블을 지원.
> 같이 보기: `asdf`.
> 더 많은 정보: <https://github.com/creationix/nvm>.

- 특정 버전의 Node.js 설치:

`nvm install {{노드_버전}}`

- 현재 셸에서 특정 버전의 Node.js 사용:

`nvm use {{노드_버전}}`

- 기본 Node.js 버전 설정:

`nvm alias default {{노드_버전}}`

- 사용 가능한 모든 Node.js 버전 나열 및 기본 버전 강조:

`nvm list`

- 지정된 Node.js 버전 제거:

`nvm uninstall {{노드_버전}}`

- 특정 버전의 Node.js REPL 실행:

`nvm run {{노드_버전}} --version`

- 특정 버전의 Node.js에서 스크립트 실행:

`nvm exec {{노드_버전}} node {{app.js}}`
