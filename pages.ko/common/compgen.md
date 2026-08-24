# compgen

> Bash에서 가능한 자동완성 후보를 생성하는 내장 명령어.
> 보통 사용자 정의 자동 완성 기능에서 사용됨.
> 관련 항목: `complete`, `compopt`.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- 실행할 수 있는 모든 쉘 내장 명령, 별칭, 함수 및 실행 파일을 표시:

`compgen -c`

- 지정한 문자열로 시작하는 실행 가능한 명령을 찾고 결과를 `$COMPREPLY`에 저장:

`compgen -V COMPREPLY -c {{문자열}}`

- 지정한 단어 목록과 일치하는 항목을 찾음:

`compgen -W "{{apple orange banana}}" {{a}}`

- 모든 별칭을 표시:

`compgen -a`

- 실행할 수 있는 모든 함수를 표시:

`compgen -A function`

- 쉘 예약 키워드를 표시:

`compgen -k`

- `ls`로 시작하는 모든 명령 또는 별칭을 표시:

`compgen -ac {{ls}}`

- 시스템의 모든 사용자 목록을 표시:

`compgen -u`
