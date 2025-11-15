# racket

> Racket 언어 인터프리터.
> 더 많은 정보: <https://docs.racket-lang.org/reference/running-sa.html#%28part._mz-cmdline%29>.

- REPL(대화형 셸) 시작:

`racket`

- Racket 스크립트 실행:

`racket {{경로/대상/스크립트.rkt}}`

- Racket 표현식 실행:

`racket --eval "{{표현식}}"`

- 모듈을 스크립트로 실행 (옵션 목록 종료):

`racket --lib {{모듈_이름}} --main {{인수}}`

- `typed/racket` 해시랭을 위한 REPL(대화형 셸) 시작:

`racket -I typed/racket`
