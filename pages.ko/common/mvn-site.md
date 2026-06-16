# mvn site

> `pom.xml` 파일에 정의된 정보를 기반으로 프로젝트 웹사이트를 생성하는 명령어.
> 더 많은 정보: <https://maven.apache.org/plugins/maven-site-plugin/usage.html>.

- site 플러그인을 사용하여 프로젝트 사이트 생성:

`mvn site`

- Maven 프로젝트의 사이트 생성 (멀티모듈 빌드):

`mvn site {{[-pl|--projects]}} {{모듈_이름}}`

- 기존 사이트 출력 정리 후 새롭게 생성:

`mvn clean site`

- 사이트 생성 시 테스트 실행 생략:

`mvn site {{[-D|--define]}} skipTests`

- 사이트를 생성 후, 원격 서버에 배포:

`mvn site-deploy`
