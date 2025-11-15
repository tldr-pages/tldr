# redis-cli

> Redis 서버에 연결합니다.
> 더 많은 정보: <https://redis.io/topics/rediscli>.

- 로컬 서버에 연결:

`redis-cli`

- 기본 포트(6379)로 원격 서버에 연결:

`redis-cli -h {{호스트}}`

- 포트 번호를 지정하여 원격 서버에 연결:

`redis-cli -h {{호스트}} -p {{포트}}`

- URI를 지정하여 원격 서버에 연결:

`redis-cli -u {{URI}}`

- 비밀번호 지정:

`redis-cli -a {{비밀번호}}`

- Redis 명령 실행:

`redis-cli {{redis_명령}}`

- 로컬 클러스터에 연결:

`redis-cli -c`
