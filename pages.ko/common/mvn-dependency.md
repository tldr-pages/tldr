# mvn dependency

> Maven 프로젝트의 의존성을 관리하고 분석하는 명령어.
> 프로젝트 의존성 조회, 해결, 복사 등의 기능을 제공.
> 더 많은 정보: <https://maven.apache.org/plugins/maven-dependency-plugin/usage.html>.

- 직접 및 전이 의존성을 포함한 전체 의존성 트리 출력:

`mvn dependency:tree`

- 의존성 분석 및 사용되지 않거나 선언되지 않은 의존성 표시:

`mvn dependency:analyze`

- 모든 프로젝트의 의존성 복사 (기본: `target/dependency/`):

`mvn dependency:copy-dependencies`

- 모든 의존성을 로컬 Maven 저장소로 다운로드:

`mvn dependency:resolve`

- 원격 저장소에서 Maven을 통해 모든 의존성 강제 업데이트:

`mvn dependency:resolve {{[-U|--update-snapshots]}}`
