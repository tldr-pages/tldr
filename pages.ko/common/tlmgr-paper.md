# tlmgr paper

> TeX Live 설치의 용지 크기 옵션 관리.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#paper>.

- 모든 TeX Live 프로그램에서 사용되는 기본 용지 크기 표시:

`tlmgr paper`

- 모든 TeX Live 프로그램의 기본 용지 크기를 A4로 설정:

`sudo tlmgr paper {{a4}}`

- 특정 TeX Live 프로그램에서 사용되는 기본 용지 크기 표시:

`tlmgr {{pdftex}} paper`

- 특정 TeX Live 프로그램의 기본 용지 크기를 A4로 설정:

`sudo tlmgr {{pdftex}} paper {{a4}}`

- 특정 TeX Live 프로그램에서 사용 가능한 모든 용지 크기 나열:

`tlmgr {{pdftex}} paper --list`

- 모든 TeX Live 프로그램에서 사용되는 기본 용지 크기를 JSON 형식으로 출력:

`tlmgr paper --json`
