# jmap

> Java 메모리 맵 도구.
> 더 많은 정보: <https://docs.oracle.com/en/java/javase/25/docs/specs/man/jmap.html>.

- Java 프로세스에 대한 공유 객체 매핑 출력 (pmap과 유사한 출력):

`jmap {{java_pid}}`

- 힙 요약 정보 출력:

`jmap -heap {{파일명.jar}} {{java_pid}}`

- 타입별 힙 사용량 히스토그램 출력:

`jmap -histo {{java_pid}}`

- 힙의 내용을 바이너리 파일로 덤프하여 jhat로 분석:

`jmap -dump:format=b,file={{경로/대상/파일}} {{java_pid}}`

- 힙의 활성 객체를 바이너리 파일로 덤프하여 jhat로 분석:

`jmap -dump:live,format=b,file={{경로/대상/파일}} {{java_pid}}`
