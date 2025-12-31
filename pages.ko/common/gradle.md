# gradle

> 오픈소스 빌드 자동화 시스템.
> 더 많은 정보: <https://manned.org/gradle>.

- 패키지 컴파일:

`gradle build`

- 테스트 작업 제외:

`gradle build -x {{test}}`

- Gradle이 빌드 중에 네트워크에 접근하지 못하도록 오프라인 모드에서 실행:

`gradle build --offline`

- 빌드 디렉터리를 삭제:

`gradle clean`

- 릴리스 모드에서 Android 패키지(APK)를 빌드:

`gradle assembleRelease`

- 주요 업무를 나열:

`gradle tasks`

- 모든 작업을 나열:

`gradle tasks --all`
