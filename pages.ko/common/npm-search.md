# npm search

> `npm` 레지스트리에서 패키지를 검색.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-search>.

- 이름으로 패키지 검색:

`npm search {{패키지}}`

- 특정 키워드로 패키지 검색:

`npm search {{키워드}}`

- 패키지 검색 시 상세 정보 포함 (예: 설명, 작성자, 버전):

`npm search {{패키지}} --long`

- 특정 작성자가 관리하는 패키지 검색:

`npm search --author {{작성자}}`

- 특정 조직의 패키지 검색:

`npm search --scope {{조직}}`

- 특정 조합의 용어로 패키지 검색:

`npm search {{용어1 용어2 ...}}`
