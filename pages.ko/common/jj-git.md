# jj git

> `jj` 저장소에서 Git 관련 명령을 실행.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-git>.

- Git 백엔드를 사용하는 새 저장소 생성:

`jj git init`

- Git 저장소를 복제하여 Git 백엔드를 사용하는 새 저장소 생성:

`jj git clone {{소스}}`

- Git 원격 저장소에서 변경 사항 가져오기:

`jj git fetch`

- 추적 중인 모든 북마크를 Git 원격 저장소로 푸시:

`jj git push`

- 지정한 북마크를 Git 원격 저장소로 푸시:

`jj git push {{[-b|--bookmark]}} {{북마크}}`
