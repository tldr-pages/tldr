# tlmgr option

> TeX Live 설정 관리자.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#option>.

- 모든 TeX Live 설정 나열:

`tlmgr option showall`

- 현재 설정된 모든 TeX Live 설정 나열:

`tlmgr option show`

- 모든 TeX Live 설정을 JSON 형식으로 출력:

`tlmgr option showall --json`

- 특정 TeX Live 설정의 값 표시:

`tlmgr option {{설정}}`

- 특정 TeX Live 설정의 값 수정:

`tlmgr option {{설정}} {{값}}`

- DVD로 설치 후 인터넷에서 향후 업데이트를 받도록 TeX Live 설정:

`tlmgr option {{저장소}} {{https://mirror.ctan.org/systems/texlive/tlnet}}`
