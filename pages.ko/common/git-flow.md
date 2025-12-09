# git flow

> 고수준 저장소 작업을 제공하는 Git 확장 모음.
> 더 많은 정보: <https://github.com/nvie/gitflow>.

- 기존 Git 저장소에서 초기화:

`git flow init`

- `develop` 브랜치를 기반으로 기능 브랜치에서 개발 시작:

`git flow feature start {{기능}}`

- 기능 브랜치에서의 개발을 완료하고, 이를 `develop` 브랜치에 병합한 후 삭제:

`git flow feature finish {{기능}}`

- 기능을 원격 서버에 게시:

`git flow feature publish {{기능}}`

- 다른 사용자가 게시한 기능 가져오기:

`git flow feature pull origin {{기능}}`
