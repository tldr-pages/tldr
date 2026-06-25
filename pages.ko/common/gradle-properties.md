# gradle properties

> Gradle 프로젝트의 속성 표시.
> 더 많은 정보: <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_project_properties>.

- 모든 프로젝트 속성 표시:

`gradle properties`

- 자세한 출력과 함께 속성 표시:

`gradle properties {{[-i|--info]}}`

- 특정 하위프로젝트의 속성 표시:

`gradle :{{하위_프로젝트}}:properties`

- 특정 속성 값 표시:

`gradle properties | grep {{속성_이름}}`
