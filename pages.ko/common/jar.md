# jar

> Java 애플리케이션/라이브러리 패키지 도구.
> 더 많은 정보: <https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>.

- 현재 디렉터리의 모든 파일을 .jar 파일로 반복적으로 아카이브:

`jar cf {{파일.jar}} *`

- .jar/.war 파일을 현재 디렉터리에 압축 해제:

`jar -xvf {{파일.jar}}`

- .jar/.war 파일 콘텐츠 나열:

`jar tf {{경로/대상/파일.jar}}`

- 자세한 출력이 포함된 .jar/.war 파일 콘텐츠 나열:

`jar tvf {{경로/대상/파일.jar}}`
