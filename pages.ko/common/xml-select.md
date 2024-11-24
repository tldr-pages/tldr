# xml select

> XPATH를 사용하여 XML 문서에서 선택.
> 팁: XML 문서의 XPATH를 표시하려면 `xml elements`를 사용하세요.
> 더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- "XPATH1"과 일치하는 모든 요소를 선택하고 그 하위 요소 "XPATH2"의 값을 출력:

`xml select --template --match "{{XPATH1}}" --value-of "{{XPATH2}}" {{경로/대상/입력.xml|URI}}`

- "XPATH1"과 일치하는 요소를 선택하고 "XPATH2"의 값을 새 줄과 함께 텍스트로 출력:

`xml select --text --template --match "{{XPATH1}}" --value-of "{{XPATH2}}" --nl {{경로/대상/입력.xml|URI}}`

- "XPATH1"의 요소 수를 계산:

`xml select --template --value-of "count({{XPATH1}})" {{경로/대상/입력.xml|URI}}`

- 하나 이상의 XML 문서에서 모든 노드 수를 계산:

`xml select --text --template --inp-name --output " " --value-of "count(node())" --nl {{경로/대상/입력1.xml|URI}} {{경로/대상/입력2.xml|URI}}`

- 도움말 표시:

`xml select --help`
