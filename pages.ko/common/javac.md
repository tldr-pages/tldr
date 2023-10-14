# javac

> 자바 애플리케이션 컴파일러.
> 더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/javac.html>.

- `.java` 파일을 컴파일:

`javac {{file.java}}`

- 여러 개의 `.java` 파일들을 컴파일:

`javac {{file1.java}} {{file2.java}} {{file3.java}}`

- 현재 디렉토리 내의 모든 `.java` 파일들을 컴파일:

`javac {{*.java}}`

- `.java` 파일을 컴파일한 후, 결과 `.class` 파일을 특정 디렉토리에 위치시키기:

`javac -d {{path/to/directory}} {{file.java}}`
