# dagger

> 로컬, CI 또는 클라우드에서 컨테이너 기반 파이프라인을 시랳ㅇ하는 프로그래밍 가능한 CI/CD 엔진.
> 더 많은 정보: <https://docs.dagger.io/reference/cli>.

- 지정한 SDK로 새로운 모듈 초기화:

`dagger init --sdk {{go|python|typescript}} {{경로/대상/모듈}}`

- 로컬 모듈을 개발 가능 상태로 준비:

`dagger develop`

- 현재 모듈에서 사용 가능한 함수 목록 표시:

`dagger functions`

- 현재 모듈의 함수 호출:

`dagger call {{함수_이름}}`

- Git 저장소로부터 모듈 의존성 설치:

`dagger install {{github.com/user/repo}}`

- 모듈 의존성 업데이트:

`dagger update`

- 도움말 표시:

`dagger {{[-h|--help]}}`

- 버전 정보 표시:

`dagger version`
