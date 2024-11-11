# xml edit

> XML 문서 편집.
> 더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- XML 문서에서 XPATH와 일치하는 요소 삭제:

`xml edit --delete "{{XPATH1}}" {{경로/대상/입력.xml|URI}}`

- XML 문서의 요소 노드를 XPATH1에서 XPATH2로 이동:

`xml edit --move "{{XPATH1}}" "{{XPATH2}}" {{경로/대상/입력.xml|URI}}`

- 이름이 "id"인 모든 속성을 "ID"로 변경:

`xml edit --rename "{{//*/@id}}" -v "{{ID}}" {{경로/대상/입력.xml|URI}}`

- "table" 요소의 하위 요소 중 "rec"으로 명명된 요소를 "record"로 이름 변경:

`xml edit --rename "{{/xml/table/rec}}" -v "{{record}}" {{경로/대상/입력.xml|URI}}`

- "id=3"인 XML 테이블 레코드를 "id=5" 값으로 업데이트:

`xml edit --update "{{xml/table/rec[@id=3]/@id}}" -v {{5}} {{경로/대상/입력.xml|URI}}`

- 도움말 표시:

`xml edit --help`
