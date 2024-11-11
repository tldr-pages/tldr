# xml format

> XML 문서를 포맷합니다.
> 더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- XML 문서를 탭으로 들여쓰기하여 포맷:

`xml format --indent-tab {{경로/대상/입력.xml|URI}} > {{경로/대상/출력.xml}}`

- HTML 문서를 4칸의 공백으로 들여쓰기하여 포맷:

`xml format --html --indent-spaces {{4}} {{경로/대상/입력.html|URI}} > {{경로/대상/출력.html}}`

- 잘못된 XML 문서에서 구문 분석이 가능한 부분을 복구하고 들여쓰지 않음:

`xml format --recover --noindent {{경로/대상/잘못된.xml|URI}} > {{경로/대상/복구된.xml}}`

- `stdin`에서 XML 문서를 포맷하고 `DOCTYPE` 선언을 제거:

`cat {{경로/대상/입력.xml}} | xml format --dropdtd > {{경로/대상/출력.xml}}`

- XML 선언을 생략하여 XML 문서를 포맷:

`xml format --omit-decl {{경로/대상/입력.xml|URI}} > {{경로/대상/출력.xml}}`

- 도움말 표시:

`xml format --help`
