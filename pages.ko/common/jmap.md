# jmap

> Java 메모리 맵 도구.
> 더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/jmap.html>.

- Java 프로세스에 대한 공유 객체 매핑 출력 (pmap과 유사한 출력):

`jmap {{자바_PID}}`

- 힙 요약 정보 출력:

`jmap -heap {{파일이름.jar}} {{자바_PID}}`

- 타입별 힙 사용량 히스토그램 출력:

`jmap -histo {{자바_PID}}`

- 힙의 내용을 이진 파일로 덤프하여 jhat으로 분석:

`jmap -dump:format=b,file={{경로/대상/파일}} {{자바_PID}}`

- 힙의 라이브 객체를 이진 파일로 덤프하여 jhat으로 분석:

`jmap -dump:live,format=b,file={{경로/대상/파일}} {{자바_PID}}`
