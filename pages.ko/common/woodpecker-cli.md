# woodpecker-cli

> Woodpecker CI 서버를 관리, 설정 및 검사하고 워크플로를 로컬에서 실행.
> 더 많은 정보: <https://woodpecker-ci.org/docs/cli>.

- 현재 프로젝트의 모든 워크플로 린트:

`woodpecker-cli lint`

- 워크플로를 로컬에서 실행:

`woodpecker-cli exec {{경로/대상/워크플로.yml}}`

- 환경 변수를 지정하여 워크플로를 로컬에서 실행:

`woodpecker-cli exec --env {{변수_이름}}={{변수_값}} {{경로/대상/워크플로.yml}}`

- 비밀값을 지정하여 워크플로를 로컬에서 실행:

`woodpecker-cli exec --secrets {{이름}}="{{값}}" {{경로/대상/워크플로.yml}}`

- 여러 비밀값을 지정하여 워크플로를 로컬에서 실행:

`woodpecker-cli exec --secrets {{이름1="값1",이름2="값2",...}} {{경로/대상/워크플로.yml}}`

- Woodpecker CI 서버를 관리하도록 명령줄 클라이언트 설정:

`woodpecker-cli setup`

- 원격 Woodpecker CI 서버에서 최근 실행된 파이프라인 표시:

`woodpecker-cli pipeline show`

- woodpecker-cli를 최신 버전으로 업데이트:

`woodpecker-cli update`
