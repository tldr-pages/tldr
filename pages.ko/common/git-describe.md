# git describe

> 사용할 수 있는 참조를 기반으로 객체에 사람이 읽을 수 있는 이름을 부여.
> 더 많은 정보: <https://git-scm.com/docs/git-describe>.

- 현재 커밋에 고유한 이름 생성 (이름에는 가장 최근의 주석이 있는 태그, 추가 커밋 수 및 약어로 된 커밋 해시가 포함됨):

`git describe`

- 약어로 된 커밋 해시에 4자리 숫자를 포함한 이름 생성:

`git describe --abbrev={{4}}`

- 태그 참조 경로로 이름 생성:

`git describe --all`

- Git 태그 설명:

`git describe {{v1.0.0}}`

- 주어진 브랜치의 마지막 커밋에 이름 생성:

`git describe {{브랜치_이름}}`
