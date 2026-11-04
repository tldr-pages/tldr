# raku

> Rakudo Raku (이전 명칭: Perl 6) 프로그래밍 언어 인터프리터.
> 관련 항목: `perl`.
> 더 많은 정보: <https://manned.org/raku>.

- Raku 스크립트 실행:

`raku {{경로/대상/스크립트.raku}}`

- 단일 Raku 명령 실행:

`raku -e "{{명령어}}"`

- 문법만 검사 (BEGIN 및 CHECK 블록은 실행됨):

`raku -c {{경로/대상/스크립트.raku}}`

- REPL (대화형 쉘) 시작:

`raku`

- 프로그램 실행 전에 모듈 로드:

`raku -M {{모듈_이름}} {{경로/대상/스크립트.raku}}`

- 모듈 검색 경로에 디렉터리 추가:

`raku -I {{경로/대상/모듈_디렉터리}} {{경로/대상/스크립트.raku}}`

- 스크립트에서 문서를 추출하여 표시:

`raku --doc {{경로/대상/스크립트.raku}}`
