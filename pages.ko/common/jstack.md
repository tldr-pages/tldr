# jstack

> Java 스택 추적 도구.
> 더 많은 정보: <https://manned.org/jstack>.

- Java 프로세스의 모든 스레드에 대한 Java 스택 추적 출력:

`jstack {{자바_PID}}`

- Java 프로세스의 모든 스레드에 대한 혼합 모드(Java/C++) 스택 추적 출력:

`jstack -m {{자바_PID}}`

- Java 코어 덤프에서 스택 추적 출력:

`jstack {{/usr/bin/java}} {{파일.core}}`
