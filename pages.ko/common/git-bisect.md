# git bisect

> 버그를 도입한 커밋을 찾기 위해 이진 탐색을 사용합니다.
> Git은 자동적으로 커밋 그래프를 왔다갔다하면서 결함이 있는 커밋을 점차적으로 좁힙니다.
> 더 많은 정보: <https://git-scm.com/docs/git-bisect>.

- 알려진 버그가 있는 커밋과 알려진 깨끗한 (일반적으로 이전) 커밋으로 제한된 커밋 범위에서 bisect 세션 시작:

`git bisect start {{bad_commit}} {{good_commit}}`

- `git bisect`가 선택한 각 커밋에 대해 이슈를 테스트한 후 "good" 또는 "bad"로 표시:

`git bisect {{good|bad}}`

- `git bisect`가 결함이 있는 커밋을 정확히 찾으면 bisect 세션을 종료하고 이전 브랜치로 돌아가기:

`git bisect reset`

- bisect 중 커밋 건너뛰기 (예: 다른 이슈로 인해 테스트가 실패하는 커밋):

`git bisect skip`

- 지금까지 수행된 작업에 대한 로그 표시:

`git bisect log`
