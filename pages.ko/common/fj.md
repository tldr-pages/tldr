# fj

> 터미널에서 Forgejo 인스턴스와 상호작용.
> 더 많은 정보: <https://codeberg.org/forgejo-contrib/forgejo-cli>.

- Forgejo 인스턴스에 로그인:

`fj auth login`

- Forgejo 저장소를 로컬에 복제:

`fj repo clone {{소유자}}/{{저장소}}`

- 현재 저장소에 새로운 이슈 생성:

`fj issue create`

- 기본 웹 브라우저에서 이슈 열기:

`fj issue browse {{이슈_번호}}`

- 새로운 pull request 생성:

`fj pr create`

- 지정한 pull request를 새로운 브랜치로 체크아웃:

`fj pr checkout {{pr_번호}}`

- 현재 저장소의 모든 릴리스 목록 표시:

`fj release list`

- 현재 인증된 사용자 정보 표시:

`fj whoami`
