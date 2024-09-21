# buku

> 명령어 브라우저 독립적인 북마크 관리자.
> 더 많은 정보: <https://github.com/jarun/Buku>.

- "키워드"와 일치하고 "개인 정보 보호" 태그가 있는 모든 북마크를 표시:

`buku {{키워드}} --stag {{개인 정보 보호}}`

- "검색 엔진" 및 "개인 정보 보호" 태그가 포함된 북마크 추가:

`buku --add {{https://example.com}} {{검색 엔진}}, {{개인 정보 보호}}`

- 북마크 삭제:

`buku --delete {{북마크_아이디}}`

- 북마크를 편집하기 위한 편집기 열기:

`buku --write {{북마크_아이디}}`

- 북마크에서 "검색 엔진" 태그 제거:

`buku --update {{북마크_아이디}} --tag {{-}} {{검색 엔진}}`