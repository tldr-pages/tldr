# mvn idea

> Maven 프로젝트를 위한 IntelliJ IDEA 프로젝트 파일(`.ipr`, `.iml`, and `.iws`)을 생성하는 명렁어.
> 참고: 이 플러그인은 더 이상 유지보수 되지 않음.
> 더 많은 정보: <https://maven.apache.org/plugins/maven-idea-plugin/usage.html>.

- 모든 IntelliJ IDEA 프로젝트 파일 생성:

`mvn idea:idea`

- 프로젝트 (`.ipr`) 파일만 생성:

`mvn idea:project`

- 워크스페이스 (`.iws`) 파일만 생성:

`mvn idea:workspace`

- 모듈 (`.iml`) 파일만 생성:

`mvn idea:module`

- 생성된 모든 프로젝트 파일 삭제:

`mvn idea:clean`
