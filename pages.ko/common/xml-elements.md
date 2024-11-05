# xml elements

> XML 문서의 요소를 추출하고 구조를 표시합니다.
> 더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- XML 문서에서 요소 추출 (XPATH 표현 생성):

`xml elements {{경로/대상/입력.xml|URI}} > {{경로/대상/요소.xpath}}`

- XML 문서에서 요소와 그 속성 추출:

`xml elements -a {{경로/대상/입력.xml|URI}} > {{경로/대상/요소.xpath}}`

- XML 문서에서 요소, 속성 및 값 추출:

`xml elements -v {{경로/대상/입력.xml|URI}} > {{경로/대상/요소.xpath}}`

- XML 문서의 정렬된 고유 요소를 출력하여 구조 확인:

`xml elements -u {{경로/대상/입력.xml|URI}}`

- 깊이 3까지의 XML 문서의 정렬된 고유 요소 출력:

`xml elements -d{{3}} {{경로/대상/입력.xml|URI}}`

- 도움말 표시:

`xml elements --help`
