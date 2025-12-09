# phing

> Apache Ant를 기반으로 한 PHP 빌드 도구.
> 더 많은 정보: <https://www.phing.info/guide/chunkhtml/ch03s03.html>.

- `build.xml` 파일에서 기본 태스크 수행:

`phing`

- 새 빌드 파일 초기화:

`phing -i {{경로/대상/build.xml}}`

- 특정 태스크 수행:

`phing {{태스크_이름}}`

- 지정된 빌드 파일 경로 사용:

`phing -f {{경로/대상/build.xml}} {{태스크_이름}}`

- 주어진 파일에 로그 기록:

`phing -logfile {{경로/대상/로그_파일}} {{태스크_이름}}`

- 빌드에서 사용자 정의 속성 사용:

`phing -D{{속성}}={{값}} {{태스크_이름}}`

- 사용자 정의 리스너 클래스 지정:

`phing -listener {{클래스_이름}} {{태스크_이름}}`

- 자세한 출력으로 빌드:

`phing -verbose {{태스크_이름}}`
