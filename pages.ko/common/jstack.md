# jstack

> Java 스택 추적 도구.
> 더 많은 정보: <https://manned.org/jstack>.

- Java 프로세스의 모든 스레드에 대한 Java 스택 추적 인쇄:

`jstack {{java_pid}}`

- Java 프로세스의 모든 스레드에 대한 혼합 모드(Java/C++) 스택 추적 인쇄:

`jstack -m {{java_pid}}`

- Java 코어 덤프에서 스택 추적 인쇄:

`jstack {{/usr/bin/java}} {{file.core}}`
