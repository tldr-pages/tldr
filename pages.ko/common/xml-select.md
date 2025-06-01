# xml select

> XPATH를 사용하여 XML 문서에서 선택.
> 팁: XML 문서의 XPATH를 표시하려면 `xml elements`를 사용하세요.
> 더 많은 정보: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139652416>.

- "XPATH1"과 일치하는 모든 요소를 선택하고 그 하위 요소 "XPATH2"의 값을 출력:

`xml {{[sel|select]}} {{[-t|--template]}} {{[-m|--match]}} "{{XPATH1}}" {{[-v|--value-of]}} "{{XPATH2}}" {{경로/대상/입력.xml|URI}}`

- "XPATH1"과 일치하는 요소를 선택하고 "XPATH2"의 값을 새 줄과 함께 텍스트로 출력:

`xml {{[sel|select]}} {{[-T|--text]}} {{[-t|--template]}} {{[-m|--match]}} "{{XPATH1}}" {{[-v|--value-of]}} "{{XPATH2}}" {{[-n|--nl]}} {{경로/대상/입력.xml|URI}}`

- "XPATH1"의 요소 수를 계산:

`xml {{[sel|select]}} {{[-t|--template]}} {{[-v|--value-of]}} "count({{XPATH1}})" {{경로/대상/입력.xml|URI}}`

- 하나 이상의 XML 문서에서 모든 노드 수를 계산:

`xml {{[sel|select]}} {{[-T|--text]}} {{[-t|--template]}} {{[-f|--inp-name]}} {{[-o|--output]}} " " {{[-v|--value-of]}} "count(node())" {{[-n|--nl]}} {{경로/대상/입력1.xml|URI}} {{경로/대상/입력2.xml|URI}}`

- 도움말 표시:

`xml {{[sel|select]}} --help`
