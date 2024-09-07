# git fetch

> 원격 저장소에서 객체와 참조를 다운로드합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-fetch>.

- 기본 원격 업스트림 저장소로부터 최신 변경 사항 가져오기 (설정된 경우):

`git fetch`

- 특정 원격 업스트림 저장소에서 새 브랜치 가져오기:

`git fetch {{remote_name}}`

- 모든 원격 업스트림 저장소에서 최신 변경 사항 가져오기:

`git fetch --all`

- 원격 업스트림 저장소에서 태그도 함께 가져오기:

`git fetch --tags`

- 업스트림에서 삭제된 원격 브랜치에 대한 로컬 참조 삭제:

`git fetch --prune`
