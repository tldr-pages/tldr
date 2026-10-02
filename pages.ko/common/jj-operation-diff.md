# jj operation diff

> 두 작업 사이에서 저장소에 발생한 변경 사항을 비교.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-diff>.

- 지정한 작업과 부모 작업 간 저장소 변경 사항 비교:

`jj {{[op|operation]}} diff {{[--op|--operation]}} {{작업_아이디}}`

- 지정한 두 작업 사이의 저장소 변경 사항 비교:

`jj {{[op|operation]}} diff {{[-f|--from]}} {{from_op}} {{[-t|--to]}} {{to_op}}`

- 변경 사항에 대한 패치를 포함해 diff를 표시:

`jj {{[op|operation]}} diff {{[-p|--patch]}} {{[--op|--operation]}} {{작업_아이디}}`

- 변경 사항을 통계 형식으로 표시:

`jj {{[op|operation]}} diff --stat {{[--op|--operation]}} {{작업_아이디}}`

- 그래프 없이 diff 표시:

`jj {{[op|operation]}} diff {{[-G|--no-graph]}} {{[--op|--operation]}} {{작업_아이디}}`
