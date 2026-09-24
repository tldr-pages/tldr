# gradle dependencyInsight

> Gradle 프로젝트의 특정 의존성에 대한 상세 정보 표시.
> 더 많은 정보: <https://docs.gradle.org/current/userguide/command_line_interface.html#reporting_dependencies>.

- 특정 의존성의 상세 정보 표시:

`gradle dependencyInsight --dependency {{패키지_이름}}`

- 특정 설정에서의 의존성 상세 정보 표시:

`gradle dependencyInsight --dependency {{패키지_이름}} --configuration {{설정_이름}}`

- 특정 하위 프로젝트의 의존성 상세 정보 표시:

`gradle :{{하위_프로젝트}}:dependencyInsight --dependency {{패키지_이름}}`

- 전체 의존성 경로를 포함한 상세 정보 표시:

`gradle dependencyInsight --dependency {{패키지_이름}} {{[-i|--info]}}`
