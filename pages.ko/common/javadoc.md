# javadoc

> 소스 코드에서 HTML 형식으로 Java API 문서 생성.
> 더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/javadoc.html>.

- Java 소스 코드에 대한 문서를 생성하고 결과를 폴더에 저장:

`javadoc -d {{경로/대상/폴더/}} {{경로/대상/자바_소스코드}}`

- 특정 인코딩으로 문서 생성:

`javadoc -docencoding {{UTF-8}} {{경로/대상/자바_소스코드}}`

- 일부 패키지를 제외한 문서 생성:

`javadoc -exclude {{패키지_목록}} {{경로/대상/자바_소스코드}}`
