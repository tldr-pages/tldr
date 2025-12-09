# git imerge

> 두 Git 브랜치 간의 병합 또는 리베이스를 점진적으로 수행.
> 브랜치 간의 충돌은 개별 커밋 쌍으로 추적되어 충돌 해결을 단순화.
> 더 많은 정보: <https://github.com/mhagger/git-imerge>.

- imerge 기반 리베이스 시작 (먼저 리베이스할 브랜치를 체크아웃):

`git imerge rebase {{리베이스할_브랜치}}`

- imerge 기반 병합 시작 (먼저 병합할 브랜치를 체크아웃):

`git imerge merge {{병합할_브랜치}}`

- 진행 중인 병합 또는 리베이스의 ASCII 다이어그램 표시:

`git imerge diagram`

- 충돌을 해결한 후 imerge 작업 계속 (`git add`로 충돌 파일을 추가한 후):

`git imerge continue --no-edit`

- 모든 충돌이 해결된 후 imerge 작업 마무리:

`git imerge finish`

- imerge 작업 중단 및 이전 브랜치로 돌아가기:

`git-imerge remove && git checkout {{이전_브랜치}}`
