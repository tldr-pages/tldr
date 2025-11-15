# gh browse

> GitHub 저장소를 브라우저에서 열거나 URL을 출력.
> 더 많은 정보: <https://cli.github.com/manual/gh_browse>.

- 현재 저장소의 홈페이지를 기본 웹 브라우저에서 열기:

`gh browse`

- 특정 저장소의 홈페이지를 기본 웹 브라우저에서 열기:

`gh browse {{소유자}}/{{저장소}}`

- 현재 저장소의 설정 페이지를 기본 웹 브라우저에서 열기:

`gh browse --settings`

- 현재 저장소의 위키를 기본 웹 브라우저에서 열기:

`gh browse --wiki`

- 특정 이슈나 풀 리퀘스트를 웹 브라우저에서 열기:

`gh browse {{이슈_번호|풀_리퀘스트_번호}}`

- 특정 브랜치를 웹 브라우저에서 열기:

`gh browse --branch {{브랜치_이름}}`

- 현재 저장소의 특정 파일이나 디렉토리를 웹 브라우저에서 열기:

`gh browse {{경로/대상/파일_또는_폴더}}`

- 웹 브라우저를 열지 않고 URL 출력:

`gh browse --no-browser`
