# html5validator

> HTML5 유효성 검증.
> 더 많은 정보: <https://github.com/svenkreiss/html5validator>.

- 특정 파일 유효성 검증:

`html5validator {{경로/대상/파일}}`

- 특정 디렉토리에 있는 모든 HTML 파일의 유효성을 검사:

`html5validator --root {{경로/대상/디렉터리}}`

- 경고와 오류 표시:

`html5validator --show-warnings {{경로/대상/파일}}`

- glob 패턴을 사용하여 여러 파일을 일치시킴:

`html5validator --root {{경로/대상/디렉터리}} --match "{{*.html *.php}}"`

- 특정 디렉터리 이름 무시:

`html5validator --root {{경로/대상/디렉터리}} --blacklist "{{node_modules vendor}}"`

- 특정 형식으로 결과를 출력:

`html5validator --format {{gnu|xml|json|text}} {{경로/대상/파일}}`

- 특정 상세 수준으로 로그를 출력:

`html5validator --root {{경로/대상/디렉터리}} --log {{debug|info|warning}}`
