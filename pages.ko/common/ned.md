# ned

> `grep`과 유사하지만 강력한 치환 기능을 제공.
> `sed`와 달리 줄 단위 편집에 제한되지 않음.
> 더 많은 정보: <https://github.com/nevdelap/ned>.

- 현재 디렉토리에서 대소문자를 무시하고 재귀적으로 검색:

`ned --ignore-case --recursive '{{^[dl]og}}' {{.}}`

- 항상 색상 출력으로 검색:

`ned --colors '{{^[dl]og}}' {{.}}`

- 색상 출력을 사용하지 않고 검색:

`ned --colors=never '{{^[dl]og}}' {{.}}`

- 특정 파일을 무시하고 검색:

`ned --recursive --exclude '{{*.htm}}' '{{^[dl]og}}' {{.}}`

- 간단한 치환:

`ned '{{dog}}' --replace '{{cat}}' {{.}}`

- 번호가 매겨진 그룹 참조를 사용한 치환:

`ned '{{the ([a-z]+) dog and the ([a-z]+) dog}}' --replace '{{the $2 dog and the $1 dog}}' {{.}}`

- 대소문자를 변경하여 치환:

`ned '{{([a-z]+) dog}}' --case-replacements --replace '{{\U$1\E! dog}}' --stdout {{.}}`

- 대상 파일을 업데이트하지 않고 찾기 및 바꾸기 결과 미리 보기:

`ned '{{^[sb]ad}}' --replace '{{happy}}' --stdout {{.}}`
