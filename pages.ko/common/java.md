# java

> 자바 애플리케이션 실행기.
> 더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/java.html>.

- 클래스 이름만 사용하여 기본 메서드가 포함된 자바 클래스 파일을 실행:

`java {{클래스 이름}}`

- 자바 프로그램을 실행하고 추가적인 타사 또는 사용자 정의 클래스 사용:

`java -classpath {{path/to/classes1}}:{{path/to/classes2}}:. {{클래스 이름}}`

- `.jar` 프로그램 실행:

`java -jar {{파일이름.jar}}`

- 포트 5005에서 연결을 기다리는 디버그를 사용하여 `.jar` 프로그램을 실행:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{파일이름.jar}}`

- JDK, JRE 및 HotSpot 버전 표시:

`java -version`

- java 명령에 대한 사용법 정보 표시:

`java -help`
