# jbang

> 독립 실행형 소스 전용 Java 프로그램을 쉽게 생성, 편집 및 실행.
> 같이 보기: `java`.
> 더 많은 정보: <https://www.jbang.dev/documentation/jbang/latest/cli/jbang.html>.

- 간단한 Java 클래스 초기화:

`jbang init {{경로/대상/파일.java}}`

- Java 클래스 초기화 (스크립팅에 유용):

`jbang init --template={{cli}} {{경로/대상/파일.java}}`

- `jshell`을 사용하여 REPL 편집기에서 스크립트 및 의존성을 탐색하고 사용:

`jbang run --interactive`

- IDE에서 스크립트를 편집할 수 있도록 임시 프로젝트 설정:

`jbang edit --open={{codium|code|eclipse|idea|netbeans|gitpod}} {{경로/대상/스크립트.java}}`

- Java 코드 스니펫 실행 (Java 9 이상):

`{{echo 'Files.list(Paths.get("/etc")).forEach(System.out::println);'}} | jbang -`

- 명령줄 애플리케이션 실행:

`jbang {{경로/대상/파일.java}} {{명령}} {{인수1 인수2 ...}}`

- 사용자의 `$PATH`에 스크립트 설치:

`jbang app install --name {{명령_이름}} {{경로/대상/스크립트.java}}`

- `jbang`과 함께 사용할 특정 버전의 JDK 설치:

`jbang jdk install {{버전}}`
