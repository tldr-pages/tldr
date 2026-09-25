# mvn generate-sources

> 메인 컴파일 단계 전에 Maven 프로젝트의 소스 코드를 생성하는 단계.
> 이 단계는 `initialize` 이후, `process-sources` 이전에 실행됨.
> 더 많은 정보: <https://manned.org/mvn>.

- `generate-sources` 단계까지 모든 라이프사이클 실행:

`mvn generate-sources`

- 다음 단계인 리소스 생성 실행:

`mvn generate-resources`

- 클린 후 소스 재생성:

`mvn clean generate-sources`
