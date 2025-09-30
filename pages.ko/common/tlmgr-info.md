# tlmgr info

> TeX Live 패키지에 대한 정보 표시.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#info>.

- 설치된 패키지에 `i`를 접두사로 붙여 모든 사용 가능한 TeX Live 패키지 나열:

`tlmgr info`

- 모든 사용 가능한 컬렉션 나열:

`tlmgr info collections`

- 모든 사용 가능한 스키마 나열:

`tlmgr info scheme`

- 특정 패키지에 대한 정보 표시:

`tlmgr info {{패키지}}`

- 특정 패키지에 포함된 모든 파일 나열:

`tlmgr info {{패키지}} --list`

- 설치된 모든 패키지 나열:

`tlmgr info --only-installed`

- 패키지에 대한 특정 정보만 표시:

`tlmgr info {{패키지}} --data "{{name}},{{category}},{{installed}},{{size}},{{depends}},..."`

- 모든 사용 가능한 패키지를 JSON 인코딩된 배열로 출력:

`tlmgr info --json`
