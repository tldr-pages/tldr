# scheme

> MIT Scheme 언어 인터프리터 및 REPL(대화형 셸).
> 더 많은 정보: <https://www.gnu.org/software/mit-scheme/documentation/stable/mit-scheme-user.html#Command_002dLine-Options>.

- REPL(대화형 셸) 시작:

`scheme`

- Scheme 프로그램 실행(REPL 출력 없음):

`scheme --quiet < {{스크립트.scm}}`

- Scheme 프로그램을 REPL에 로드:

`scheme --load {{스크립트.scm}}`

- Scheme 표현식을 REPL에 로드:

`scheme --eval "{{(define foo 'x)}}"`

- 조용한 모드로 REPL 열기:

`scheme --quiet`
