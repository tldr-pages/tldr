# git init

> 새로운 로컬 Git 저장소를 초기화합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-init>.

- 새로운 로컬 저장소 초기화:

`git init`

- 초기 브랜치에 지정된 이름을 가진 저장소를 초기화:

`git init --initial-branch={{branch_name}}`

- 객체 해시로 SHA256를 사용하여 저장소 초기화 (Git 버전 2.29+ 이상 필요):

`git init --object-format={{sha256}}`

- SSH를 통해 원격으로 사용할 수 있는 베어본 저장소 초기화:

`git init --bare`
