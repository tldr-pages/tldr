# gradle init

> 새로운 Gradle 프로젝트를 대화형으로 초기화.
> 더 많은 정보: <https://docs.gradle.org/current/userguide/build_init_plugin.html>.

- 새로운 Gradle 프로젝트를 대화형으로 초기화:

`gradle init`

- 특정 유형의 프로젝트 초기화:

`gradle init --type {{basic|java-application|java-library|...}}`

- 특정 DSL로 프로젝트 초기화:

`gradle init --dsl {{groovy|kotlin}}`

- 특정 테스트 프레임워크로 프로젝트 초기화:

`gradle init --test-framework {{junit-jupiter|testng|spock}}`

- 대화형 입력 없이 프로젝트 초기화:

`gradle init --type {{java-application}} --dsl {{kotlin}} --test-framework {{junit-jupiter}}`
