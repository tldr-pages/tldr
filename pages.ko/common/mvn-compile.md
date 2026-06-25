# mvn compile

> Maven 프로젝트의 소스 코드를 컴파일하는 명령어.
> 더 많은 정보: <https://manned.org/mvn>.

- 프로젝트 소스 코드 컴파일:

`mvn compile`

- 컴파일 결과를 정리한 후 다시 컴파일:

`mvn clean compile`

- 멀티 모듈 프로젝트에서 특정 모듈만 컴파일:

`mvn compile {{[-pl|--projects]}} {{모듈_이름}}`

- 테스트를 건너뛰고 컴파일:

`mvn compile {{[-D|--define]}} skipTests`
