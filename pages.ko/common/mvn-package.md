# mvn package

> Package the compiled code of a Maven project into its distributable format (such as a `.jar` or `.war`).
> More information: <https://manned.org/mvn>.

- 프로젝트 패키징:

`mvn package`

- 테스트 실행을 건너뛰고 패키징:

`mvn package {{[-D|--define]}} skipTests`

- 모든 의존성을 강제 업데이트하면서 패키징:

`mvn package {{[-U|--update-snapshots]}}`
