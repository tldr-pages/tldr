# xml format

> XML 문서를 포맷합니다.
> 더 많은 정보: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139569312>.

- XML 문서를 탭으로 들여쓰기하여 포맷:

`xml {{[fo|format]}} {{[-t|--indent-tab]}} {{경로/대상/입력.xml|URI}} > {{경로/대상/출력.xml}}`

- HTML 문서를 4칸의 공백으로 들여쓰기하여 포맷:

`xml {{[fo|format]}} {{[-H|--html]}} {{[-s|--indent-spaces]}} {{4}} {{경로/대상/입력.html|URI}} > {{경로/대상/출력.html}}`

- 잘못된 XML 문서에서 구문 분석이 가능한 부분을 복구하고 들여쓰지 않음:

`xml {{[fo|format]}} {{[-R|--recover]}} {{[-n|--noindent]}} {{경로/대상/잘못된.xml|URI}} > {{경로/대상/복구된.xml}}`

- `stdin`에서 XML 문서를 포맷하고 `DOCTYPE` 선언을 제거:

`cat {{경로/대상/입력.xml}} | xml {{[fo|format]}} {{[-D|--dropdtd]}} > {{경로/대상/출력.xml}}`

- XML 선언을 생략하여 XML 문서를 포맷:

`xml {{[fo|format]}} {{[-o|--omit-decl]}} {{경로/대상/입력.xml|URI}} > {{경로/대상/출력.xml}}`

- 도움말 표시:

`xml {{[fo|format]}} --help`
