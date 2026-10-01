# jj operation show

> 작업에서 발생한 저장소 변경 사항 표시.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-show>.

- 현재 작업과 부모 작업 간 저장소 변경 사항 표시:

`jj {{[op|operation]}} show`

- 지정한 작업의 저장소 변경 사항 표시:

`jj {{[op|operation]}} show {{작업_아이디}}`

- 패치 세부 정보와 함께 저장소 변경 사항 표시:

`jj {{[op|operation]}} show {{[-p|--patch]}} {{작업_아이디}}`

- 작업에서 변경된 경로의 요약 표시:

`jj {{[op|operation]}} show {{[-s|--summary]}} {{작업_아이디}}`

- 작업 변경 사항 통계(히스토그램) 표시:

`jj {{[op|operation]}} show --stat {{작업_아이디}}`

- 그래프 없이 변경 사항 표시:

`jj {{[op|operation]}} show {{[-G|--no-graph]}} {{작업_아이디}}`
