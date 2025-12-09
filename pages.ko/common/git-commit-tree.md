# git commit-tree

> Git의 내부 동작을 직접 다루는 명령어로, 커밋 객체를 직접 생성합니다.
> 참조: `git commit`.
> 더 많은 정보: <https://git-scm.com/docs/git-commit-tree>.

- 지정된 메시지로 커밋 객체 생성:

`git commit-tree {{tree}} -m "{{message}}"`

- 지정된 파일의 내용을 커밋 메시지로 사용하여 커밋 객체 생성 (`stdin`의 경우 `-` 사용):

`git commit-tree {{tree}} -F {{path/to/file}}`

- GPG 키로 인증된 커밋 객체 생성:

`git commit-tree {{tree}} -m "{{message}}" {{[-S|--gpg-sign]}}`

- 지정된 부모 커밋 객체를 가진 커밋 객체 생성:

`git commit-tree {{tree}} -m "{{message}}" -p {{parent_commit_sha}}`
