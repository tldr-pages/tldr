# hut

> sourcehut용 CLI 도구.
> 더 많은 정보: <https://manned.org/hut>.

- `hut`의 구성 파일을 초기화 (`hut`를 사용하는 데 필요한 OAuth2 액세스 토큰을 묻는 메시지가 표시됨):

`hut init`

- Git/Mercurial 저장소 나열:

`hut {{git|hg}} list`

- 공개 Git/Mercurial 저장소를 생성:

`hut {{git|hg}} create {{이름}}`

- <https://builds.sr.ht>의 작업 목록 나열:

`hut builds list`

- 작업 상태 표시:

`hut builds show {{작업_아이디}}`

- 작업 컨테이너에 SSH로 연결:

`hut ssh {{작업_아이디}}`
