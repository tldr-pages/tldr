# jhat

> Java 힙 분석 도구.
> 더 많은 정보: <https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jhat.html>.

- 힙 덤프(`jmap`에서 생성)를 분석하고, HTTP를 통해 포트 7000에서 보기:

`jhat {{덤프_파일.bin}}`

- 힙 덤프를 분석하고, HTTP 서버의 대체 포트를 지정:

`jhat -p {{포트}} {{덤프_파일.bin}}`

- 최대 8GB RAM을 사용하여 덤프를 분석 (`jhat` 사용 권장 2-4배 덤프 크기):

`jhat -J-mx8G {{덤프_파일.bin}}`
