# jdeps

> Java 클래스 종속성 분석기.
> 더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/jdeps.html>.

- `.jar` 또는 `.class` 파일의 종속성 분석:

`jdeps {{경로/대상/파일명.class}}`

- 특정 `.jar` 파일의 모든 종속성 요약 출력:

`jdeps {{경로/대상/파일명.jar}} -summary`

- `.jar` 파일의 모든 클래스 수준 종속성 출력:

`jdeps {{경로/대상/파일명.jar}} -verbose`

- 분석 결과를 DOT 파일로 특정 디렉토리에 출력:

`jdeps {{경로/대상/파일명.jar}} -dotoutput {{경로/대상/폴더}}`

- 도움말 표시:

`jdeps --help`
