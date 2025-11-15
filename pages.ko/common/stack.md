# stack

> Haskell 프로젝트 관리 도구.
> 더 많은 정보: <https://github.com/commercialhaskell/stack>.

- 새 패키지 생성:

`stack new {{패키지}} {{템플릿}}`

- 패키지 컴파일:

`stack build`

- 패키지 내 테스트 실행:

`stack test`

- 프로젝트를 컴파일하고 파일이 변경될 때마다 다시 컴파일:

`stack build --file-watch`

- 프로젝트 컴파일 후 명령 실행:

`stack build --exec "{{명령}}"`

- 프로그램을 실행하고 인수를 전달:

`stack exec {{프로그램}} -- {{인수}}`
