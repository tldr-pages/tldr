# mvn package

> Maven 프로젝트의 컴파일된 코드를 배포 가능한 형식(`.jar`, `.war` 등)으로 패키징.
> 더 많은 정보: <https://manned.org/mvn>.

- 프로젝트 패키징:

`mvn package`

- 테스트 실행을 건너뛰고 패키징:

`mvn package {{[-D|--define]}} skipTests`

- 모든 의존성을 강제 업데이트하면서 패키징:

`mvn package {{[-U|--update-snapshots]}}`
