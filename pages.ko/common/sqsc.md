# sqsc

> 명령줄 AWS Simple Queue Service 클라이언트.
> 더 많은 정보: <https://github.com/yongfei25/sqsc>.

- 모든 큐 나열:

`sqsc lq {{큐_접두사}}`

- 큐에 있는 모든 메시지 나열:

`sqsc ls {{큐_이름}}`

- 한 큐의 모든 메시지를 다른 큐로 복사:

`sqsc cp {{소스_큐}} {{대상_큐}}`

- 한 큐의 모든 메시지를 다른 큐로 이동:

`sqsc mv {{소스_큐}} {{대상_큐}}`

- 큐 설명:

`sqsc describe {{큐_이름}}`

- SQL 구문을 사용하여 큐 조회:

`sqsc query "SELECT body FROM {{큐_이름}} WHERE body LIKE '%user%'"`

- 현재 작업 디렉토리의 로컬 SQLite 데이터베이스로 큐의 모든 메시지 가져오기:

`sqsc pull {{큐_이름}}`
