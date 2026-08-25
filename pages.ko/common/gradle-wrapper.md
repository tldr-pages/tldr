# gradle wrapper

> 프로젝트용 Gradle Wrapper 파일 생성.
> 더 많은 정보: <https://docs.gradle.org/current/userguide/gradle_wrapper.html>.

- 현재 Gradle 버전으로 wrapper 생성:

`gradle wrapper`

- 특정 Gradle 버전으로 wrapper 생성:

`gradle wrapper --gradle-version {{8.5}}`

- 특정 배포 타입으로 wrapper 생성:

`gradle wrapper --distribution-type {{bin|all}}`

- 특정 배포 URL을 사용하여 wrapper 생성:

`gradle wrapper --gradle-distribution-url {{주소}}`
