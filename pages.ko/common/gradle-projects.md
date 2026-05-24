# gradle projects

> Gradle 프로젝트의 하위 프로젝트 목록 표시.
> 더 많은 정보: <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_projects>.

- 모든 하위프로젝트 표시:

`gradle projects`

- 설명과 함께 하위 프로젝트 표시:

`gradle projects {{[-i|--info]}}`

- 멀티 프로젝트 빌드에서 특정 프로젝트의 하위 프로젝트 표시:

`gradle :{{하위_프로젝트}}:projects`
