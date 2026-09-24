# cut

> `stdin` 또는 파일에서 특정 필드를 잘라내기.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html>.

- 각 줄에서 5번째 문자를 출력:

`{{명령어}} | cut {{[-c|--characters]}} 5`

- 지정한 파일의 각 줄에서 5~10번째 문자까지 출력:

`cut {{[-c|--characters]}} 5-10 {{경로/대상/파일}}`

- 파일의 각 줄을 구분자로 나누어 필드로 나누고, 2번째와 6번째 필드를 출력 (기본 구분자는 `TAB`):

`cut {{[-f|--fields]}} 2,6 {{경로/대상/파일}}`

- 지정한 구분자로 각 줄을 분리하고 두 번째 필드로부터 끝까지 출력:

`{{명령어}} | cut {{[-d|--delimiter]}} "{{구분자}}" {{[-f|--fields]}} 2-`

- 공백을 구분자로 사용하여 처음 3개의 필드만 출력:

`{{명령어}} | cut {{[-d|--delimiter]}} " " {{[-f|--fields]}} -3`

- 구분자를 포함하는 줄만 출력:

`{{명령어}} | cut {{[-d|--delimiter]}} "{{:}}" {{[-f|--fields]}} {{1}} {{[-s|--only-delimited]}}`

- 줄 구분자로 개행 대신 `NUL`을 사용하는 경우 특정 필드를 출력:

`{{find . -print0}} | cut {{[-z|--zero-terminated]}} {{[-d|--delimiter]}} "{{/}}" {{[-f|--fields]}} {{2}}`
