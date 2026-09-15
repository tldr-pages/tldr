# jj operation

> `jj` 저장소의 작업 로그를 관리.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation>.

- 작업 로그 표시:

`jj {{[op|operation]}} log`

- 마지막 작업 실행 취소:

`jj {{[op|operation]}} undo`

- 지정한 작업 실행 취소:

`jj {{[op|operation]}} undo {{작업}}`

- 저장소를 지정한 작업 시점의 상태로 복원:

`jj {{[op|operation]}} restore {{작업}}`

- 지정한 작업에서 저장소에 적용된 변경 사항 표시:

`jj {{[op|operation]}} show {{작업}}`

- 지정한 작업의 변경 사항 통계, 요약 및 패치 표시:

`jj {{[op|operation]}} show {{--stat}} {{[-s|--summary]}} {{[-p|--patch]}} {{작업}}`
