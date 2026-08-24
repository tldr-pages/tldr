# gradle tasks

> Gradle 프로젝트에서 사용 가능한 작업 목록 표시.
> 더 많은 정보: <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_tasks>.

- 주요 작업 목록 표시:

`gradle tasks`

- 하위 작업을 포함한 모든 작업 목록 표시:

`gradle tasks --all`

- 특정 그룹의 작업 목록 표시:

`gradle tasks --group {{그룹_이름}}`

- 특정 하위 프로젝트의 작업 목록 표시:

`gradle :{{하위_프로젝트}}:tasks`
