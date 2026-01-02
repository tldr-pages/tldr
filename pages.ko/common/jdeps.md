# jdeps

> Java 클래스 의존성 분석기.
> 더 많은 정보: <https://docs.oracle.com/en/java/javase/25/docs/specs/man/jdeps.html>.

- `.jar` 또는 `.class` 파일의 의존성을 분석:

`jdeps {{경로/대상/파일이름.class}}`

- 특정 `.jar` 파일의 모든 의존성 요약 표시:

`jdeps {{경로/대상/파일이름.jar}} -summary`

- `.jar` 파일의 모든 클래스 레벨 의존성 표시:

`jdeps {{경로/대상/파일이름.jar}} -verbose`

- 분석 결과를 특정 디렉토리에 DOT 파일로 출력:

`jdeps {{경로/대상/파일이름.jar}} -dotoutput {{경로/대상/폴더}}`

- 도움말 표시:

`jdeps --help`
