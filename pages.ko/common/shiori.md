# shiori

> Go로 제작된 간단한 북마크 관리자.
> 더 많은 정보: <https://github.com/go-shiori/shiori/blob/master/docs/Usage.md>.

- HTML 넷스케이프 북마크 형식 파일에서 북마크 가져오기:

`shiori import {{경로/대상/북마크들.html}}`

- 지정된 URL을 북마크로 저장:

`shiori add {{url}}`

- 저장된 북마크 나열:

`shiori print`

- 저장된 북마크를 브라우저에서 열기:

`shiori open {{북마크_id}}`

- 포트 8181에서 북마크 관리를 위한 웹 인터페이스 시작:

`shiori serve --port {{8181}}`
