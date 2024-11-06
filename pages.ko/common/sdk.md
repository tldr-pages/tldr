# sdk

> 여러 소프트웨어 개발 키트의 병렬 버전을 관리.
> Java, Groovy, Scala, Kotlin, Gradle, Maven, Vert.x 등 여러 언어를 지원.
> 더 많은 정보: <https://sdkman.io/usage>.

- SDK 버전 설치:

`sdk install {{sdk_이름}} {{sdk_버전}}`

- 현재 터미널 세션에서 특정 SDK 버전 사용:

`sdk use {{sdk_이름}} {{sdk_버전}}`

- 사용 가능한 SDK의 안정적인 버전 표시:

`sdk current {{sdk_이름}}`

- 설치된 모든 SDK의 안정적인 버전 표시:

`sdk current`

- 사용 가능한 모든 SDK 나열:

`sdk list`

- 특정 SDK의 모든 버전 나열:

`sdk list {{sdk_이름}}`

- SDK를 최신 안정 버전으로 업그레이드:

`sdk upgrade {{sdk_이름}}`

- 특정 SDK 버전 제거:

`sdk rm {{sdk_이름}} {{sdk_버전}}`
