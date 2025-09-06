# dash

> Debian Almquist Shell은 `sh`의 최신 POSIX 호환 구현 (Bash와 호환되지 않음).
> 더 많은 정보: <https://manned.org/dash>.

- 대화형 쉘 세션을 시작:

`dash`

- 특정 명령어([c]ommands)를 실행:

`dash -c "{{echo 'dash가 실행중'}}"`

- 특정 스크립트 실행:

`dash {{경로/대상/스크립트.sh}}`

- 구문 오류가 있는지 특정 스크립트를 확인:

`dash -n {{경로/대상/스크립트.sh}}`

- 실행하기 전에 각 명령을 출력하는 동안 특정 스크립트를 실행:

`dash -x {{경로/대상/스크립트.sh}}`

- 특정 스크립트를 실행하고 첫 번째 오류([e]rror)에서 중지:

`dash -e {{경로/대상/스크립트.sh}}`

- `stdin`에서 특정 명령을 실행:

`{{echo "echo 'dash가 실행중'"}} | dash`
