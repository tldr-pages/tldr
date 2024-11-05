# optipng

> PNG 파일 최적화 도구.
> 더 많은 정보: <https://optipng.sourceforge.net>.

- 기본 설정으로 PNG 압축:

`optipng {{경로/대상/파일.png}}`

- 최상의 압축으로 PNG 압축:

`optipng -o{{7}} {{경로/대상/파일.png}}`

- 가장 빠른 압축으로 PNG 압축:

`optipng -o{{0}} {{경로/대상/파일.png}}`

- PNG를 압축하고 인터레이싱 추가:

`optipng -i {{1}} {{경로/대상/파일.png}}`

- PNG를 압축하고 모든 메타데이터(파일 타임스탬프 포함) 보존:

`optipng -preserve {{경로/대상/파일.png}}`

- PNG를 압축하고 모든 메타데이터 제거:

`optipng -strip all {{경로/대상/파일.png}}`
