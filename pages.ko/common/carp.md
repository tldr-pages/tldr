# carp

> Carp용 REPL 및 빌드 도구.
> 더 많은 정보: <https://carp-lang.github.io/carp-docs/Manual.html>.

- REPL (대화형 셸)을 시작:

`carp`

- 사용자 정의 프롬프트로 REPL을 시작:

`carp --prompt "{{> }}"`

- `carp` 파일을 빌드:

`carp -b {{경로/대상/파일.carp}}`

- 파일 빌드 및 실행:

`carp -x {{경로/대상/파일.carp}}`

- 최적화가 활성화된 파일을 빌드:

`carp -b --optimize {{경로/대상/파일.carp}}`

- 파일을 C 코드로 변환:

`carp --generate-only {{경로/대상/파일.carp}}`
