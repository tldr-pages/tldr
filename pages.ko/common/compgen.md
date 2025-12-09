# compgen

> `<Tab>` 키를 두 번 누르면 호출되는 Bash의 자동 완성 명령이 내장.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- 실행할 수 있는 모든 명령을 나열:

`compgen -c`

- 모든 별칭을 나열:

`compgen -a`

- 실행할 수 있는 모든 기능을 나열:

`compgen -A function`

- 쉘 예약 키워드 표시:

`compgen -k`

- 'ls'로 시작하는 사용 가능한 모든 명령/별칭을 확인:

`compgen -ac {{ls}}`
