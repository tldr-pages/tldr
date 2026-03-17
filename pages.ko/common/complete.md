# complete

> Bash에서 쉘 명령의 인자 자동 완성 규측을 조회하고 설정.
> Bash에서 `<Tab>` 키를 누르면 지정된 자동 완성이 실행됨.
> 관련 항목: `compgen`, `compopt`.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-complete>.

- 함수를 사용해 명령의 인자 자동완성을 설정 (완성 결과는 `$COMPREPLY` 변수에 저장됨):

`complete -F {{함수}} {{명령어}}`

- 다른 명령을 사용하여 인자 자동완성을 설정 (`$1`은 명령, `$2`는 현재 커서가 위치한 인자, `$3`은 커서 앞의 인자):

`complete -C {{자동완성_명령어}} {{명령어}}`

- 명령의 인자를 쉘 내장 명령으로 자동 완성하도록 설정:

`complete -b {{명령어}}`

- 완성된 단어 뒤에 공백을 추가하지 않고 자동완성을 적용:

`complete -o nospace -F {{함수}} {{명령어}}`

- 로드된 모든 자동완성 설정을 표시:

`complete -p`

- 특정 명령의 자동완성 설정을 표시:

`complete -p {{명령어}}`
