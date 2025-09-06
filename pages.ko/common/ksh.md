# ksh

> Korn Shell, Bash와 호환되는 명령줄 인터프리터.
> 같이 보기: `histexpand`.
> 더 많은 정보: <https://manned.org/ksh>.

- 대화형 셸 세션 시작:

`ksh`

- 특정 [c]명령어 실행:

`ksh -c "{{echo 'ksh is executed'}}"`

- 특정 스크립트 실행:

`ksh {{경로/대상/스크립트.ksh}}`

- 특정 스크립트를 실행하지 않고 구문 오류 검사:

`ksh -n {{경로/대상/스크립트.ksh}}`

- 특정 스크립트를 실행하면서 각 명령을 실행 전 출력:

`ksh -x {{경로/대상/스크립트.ksh}}`
