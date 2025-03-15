# expect

> 사용자 입력이 필요한 다른 프로그램과 상호작용하는 스크립트 실행기.
> 더 많은 정보: <https://manned.org/expect>.

- 파일에서 expect 스크립트 실행:

`expect {{경로/대상/파일}}`

- 지정된 expect 스크립트 실행:

`expect -c "{{명령어들}}"`

- 대화형 REPL 모드로 진입 (`exit` 또는 `<Ctrl d>`로 종료):

`expect -i`
