# mvn install

> 서드파티 Maven 의존성을 설치하고 프로젝트를 빌드.
> 더 많은 정보: <https://manned.org/mvn>.

- 컴파일, 테스트, 패키징 후 로컬 저장소에 설치:

`mvn install`

- 설치 과정에서 테스트 실행 생략:

`mvn install {{[-D|--define]}} skipTests`

- 설치 전에 의존성 강제 업데이트:

`mvn install {{[-U|--update-snapshots]}}`

- 테스트 컴파일 및 실행 모두 생략:

`mvn install {{[-D|--define]}} maven.test.skip=true`
