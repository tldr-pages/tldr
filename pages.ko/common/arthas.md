# arthas

> Java 진단 도구.
> 함께 보기: `arthas-watch`, `arthas-trace`.
> 더 많은 정보: <https://arthas.aliyun.com/en/>.

- Arthas를 시작:

`java -jar {{경로/대상/arthas-boot.jar}}`

- Arthas에 다시 연결 (Arthas의 기본 포트는 3658):

`telnet localhost {{포트_번호}}`

- 현재 Arthas 클라이언트를 종료합니다. 다른 클라이언트에는 영향을 주지 않음(`exit`、`logout`、`q` 명령과 동일):

`{{exit|quit|logout|q}}`

- Arthas 서버를 종료합니다. 이 서버에 연결된 모든 Arthas 클라이언트의 연결 종료:

`stop`
