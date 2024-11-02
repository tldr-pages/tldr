# jhsdb

> Java 프로세스에 연결하거나 충돌한 Java 가상 머신의 코어 덤프를 분석하기 위한 사후 디버거를 시작.
> 더 많은 정보: <https://manned.org/jhsdb>.

- Java 프로세스의 스택 및 잠금 정보 출력:

`jhsdb jstack --pid {{pid}}`

- 대화형 디버그 모드에서 코어 덤프 열기:

`jhsdb clhsdb --core {{경로/대상/코어_덤프}} --exe {{경로/대상/jdk/bin/java}}`

- 원격 디버그 서버 시작:

`jhsdb debugd --pid {{pid}} --serverid {{선택적_고유_ID}}`

- 대화형 디버그 모드에서 프로세스에 연결:

`jhsdb clhsdb --pid {{pid}}`
