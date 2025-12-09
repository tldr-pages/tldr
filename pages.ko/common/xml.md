# xml

> XMLStarlet 도구 모음: XML 문서를 쿼리, 편집, 검사, 변환 및 변형.
> `xml validate`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139670224>.

- 하위 명령 목록을 포함한 일반 도움말 표시:

`xml --help`

- 파일 또는 URI에서 입력을 받아 `stdout`에 출력하여 하위 명령 실행:

`xml {{하위_명령}} {{옵션}} {{경로/대상/입력.xml|URI}}`

- `stdin`과 `stdout`을 사용하여 하위 명령 실행:

`xml {{하위_명령}} {{옵션}}`

- 파일 또는 URI에서 입력을 받아 파일로 출력하여 하위 명령 실행:

`xml {{하위_명령}} {{옵션}} {{경로/대상/입력.xml|URI}} > {{경로/대상/출력}}`

- 특정 하위 명령에 대한 도움말 표시:

`xml {{하위_명령}} --help`

- 버전 표시:

`xml --version`
