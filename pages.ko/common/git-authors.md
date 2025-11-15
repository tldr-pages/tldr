# git authors

> Git 저장소의 커밋 작성자 목록을 생성.
> `git-extras`의 일부.
> 더 많은 정보: <https://manned.org/git-authors>.

- 커밋 작성자 목록을 `AUTHORS` 파일 대신 `stdout`에 출력:

`git authors {{[-l|--list]}}`

- 커밋 작성자 목록을 `AUTHORS` 파일에 추가하고 기본 편집기로 열기:

`git authors`

- 이메일 주소를 제외한 커밋 작성자 목록을 `AUTHORS` 파일에 추가하고 기본 편집기로 열기:

`git authors --no-email`
