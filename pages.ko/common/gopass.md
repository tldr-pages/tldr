# gopass

> 팀을 위한 표준 Unix 비밀번호 관리자. Go 언어로 작성됨.
> 더 많은 정보: <https://www.gopass.pw>.

- 구성 설정을 초기화:

`gopass init`

- 새로운 항목 생성:

`gopass new`

- 모든 저장소 보기:

`gopass mounts`

- 공유 Git 저장소 마운트:

`gopass mounts add {{저장소_이름}} {{git_레포지토리_주소}}`

- 키워드를 사용해 대화형으로 검색:

`gopass show {{키워드}}`

- 키워드를 사용해 검색:

`gopass find {{키워드}}`

- 마운트된 모든 저장소 동기화:

`gopass sync`

- 특정 비밀번호 항목을 표시:

`gopass {{저장소_이름|경로/대상/디렉터리|이메일@email.com}}`
