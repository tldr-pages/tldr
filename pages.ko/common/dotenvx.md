# dotenvx

> `dotenv`의 제작자가 만든 더 개선된 `dotenv` 도구.
> 더 많은 정보: <https://dotenvx.com/docs/>.

- `.env` 파일의 환경 변수를 사용하여 명령 실행:

`dotenvx run -- {{명령어}}`

- 특정 `.env` 파일의 환경 변수를 사용하여 명령 실행:

`dotenvx run -f {{경로/대상/파일.env}} -- {{명령어}}`

- 환경 변수를 암호화하여 설정:

`dotenvx set {{키}} {{값}}`

- 환경 변수를 암호화 없이 설정:

`dotenvx set {{키}} {{값}} --plain`

- `.env` 파일에 정의된 환경 변수 조회:

`dotenvx get`

- `.env` 파일에 정의된 특정 환경 변수 값 조회:

`dotenvx get {{키}}`

- `.env` 파일과 OS의 모든 환경 변수 조회:

`dotenvx get --all`
