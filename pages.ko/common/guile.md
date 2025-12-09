# guile

> Guile 스키마 해석기.
> 더 많은 정보: <https://www.gnu.org/software/guile/manual/guile.html#Invoking-Guile>.

- REPL(대화형 쉘)을 시작:

`guile`

- 지정된 스키마 파일에서 스크립트를 실행:

`guile {{스크립트.scm}}`

- 스키마 표현식 실행:

`guile -c "{{표현식}}"`

- 원격 REPL 연결을 위해 포트 또는 Unix 도메인 소켓(기본값은 37146포트):

`guile --listen={{포트_또는_소켓}}`
