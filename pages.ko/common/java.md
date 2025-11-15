# java

> Java 애플리케이션 실행기.
> 더 많은 정보: <https://docs.oracle.com/en/java/javase/25/docs/specs/man/java.html>.

- 메인 메서드를 포함한 Java `.class` 파일을 클래스 이름만 사용하여 실행:

`java {{클래스명}}`

- 추가 서드파티 또는 사용자 정의 클래스를 사용하여 Java 프로그램 실행:

`java -classpath {{경로/대상/클래스1}}:{{경로/대상/클래스2}}:. {{클래스명}}`

- `.jar` 프로그램 실행:

`java -jar {{파일명.jar}}`

- 포트 5005에서 연결 대기 상태로 디버그 모드에서 `.jar` 프로그램 실행:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{파일명.jar}}`

- JDK, JRE 및 HotSpot 버전 표시:

`java -version`

- 도움말 표시:

`java -help`
