# texconfig

> TeX Live 또는 teTeX를 설정.
> 많은 경우 `tlmgr`로 대체됨.
> 더 많은 정보: <https://manned.org/texconfig>.

- 현재 TeX 설정 표시:

`texconfig conf`

- 지원되는 프로그램의 기본 용지 크기 설정:

`texconfig paper {{a4|letter|...}}`

- PDFTeX의 기본 용지 크기 설정:

`texconfig pdftex paper {{a4|letter|...}}`

- 모든 TeX 포맷과 글꼴 맵 다시 생성:

`texconfig init`

- 지정한 포맷 다시 생성:

`texconfig init {{포맷}}`

- TeX 파일 이름 데이터베이스 새로 고침:

`texconfig rehash`
