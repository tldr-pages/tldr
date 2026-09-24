# gradle build

> Gradle을 사용하여 프로젝트 빌드.
> 더 많은 정보: <https://docs.gradle.org/current/userguide/command_line_interface.html#common_tasks>.

- 프로젝트 빌드 수행:

`gradle build`

- clean 빌드 수행:

`gradle clean build`

- 테스트를 제외하고 프로젝트 빌드:

`gradle build {{[-x|--exclude-task]}} test`

- 더 자세한 로그와 함께 Build 수행:

`gradle build {{[-i|--info]}}`
