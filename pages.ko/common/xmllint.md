# xmllint

> XPath를 지원하는 XML 파서 및 린터로, XML 트리를 탐색할 수 있는 구문입니다.
> 더 많은 정보: <https://manned.org/xmllint>.

- 이름이 "foo"인 모든 노드(태그) 반환:

`xmllint --xpath "//{{foo}}" {{소스_파일.xml}}`

- 이름이 "foo"인 첫 번째 노드의 내용을 문자열로 반환:

`xmllint --xpath "string(//{{foo}})" {{소스_파일.xml}}`

- HTML 파일에서 두 번째 앵커 요소의 href 속성 반환:

`xmllint --html --xpath "string(//a[2]/@href)" webpage.xhtml`

- 파일에서 사람이 읽을 수 있는(들여쓰기 된) XML 반환:

`xmllint --format {{소스_파일.xml}}`

- XML 파일이 DOCTYPE 선언의 요구 사항을 충족하는지 확인:

`xmllint --valid {{소스_파일.xml}}`

- 온라인에 호스팅된 DTD 스키마에 대해 XML 유효성 검사:

`xmllint --dtdvalid {{URL}} {{소스_파일.xml}}`
