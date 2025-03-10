# look

> 정렬된 파일에서 특정 접두사로 시작하는 줄을 표시합니다.
> 같이 보기: `grep`, `sort`.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/look.1.html>.

- 특정 파일에서 특정 접두사로 시작하는 줄 검색:

`look {{접두사}} {{경로/대상/파일}}`

- 대소문자를 구분하지 않고 영숫자 문자만 검색:

`look {{[-f|--ignore-case]}} {{[-d|--alphanum]}} {{접두사}} {{경로/대상/파일}}`

- 문자열 종료 문자를 지정 (기본값은 공백):

`look {{[-t|--terminate]}} {{,}}`

- `/usr/share/dict/words`에서 검색 (`--ignore-case` 및 `--alphanum` 기본 적용):

`look {{접두사}}`
