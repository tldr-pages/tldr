# gradle test

> Gradle을 사용해 테스트 실행.
> 더 많은 정보: <https://docs.gradle.org/current/userguide/java_testing.html>.

- 모든 테스트 실행:

`gradle test`

- 자세한 출력과 함께 테스트 실행:

`gradle test {{[-i|--info]}}`

- 특정 테스트 클래스 실행:

`gradle test --tests {{클래스_이름}}`

- 패턴과 일치하는 테스트 실행:

`gradle test --tests "{{패턴}}"`

- 최신 상태여도 테스트 다시 실행:

`gradle test --rerun`
