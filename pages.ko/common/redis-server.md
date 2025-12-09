# redis-server

> 영구적인 키-값 데이터베이스.
> 더 많은 정보: <https://redis.io/learn/operate/redis-at-scale/talking-to-redis/configuring-a-redis-server>.

- 기본 포트(6379)를 사용하여 Redis 서버 시작 및 로그를 `stdout`으로 출력:

`redis-server`

- 기본 포트를 사용하여 백그라운드 프로세스로 Redis 서버 시작:

`redis-server --daemonize yes`

- 지정된 포트를 사용하여 백그라운드 프로세스로 Redis 서버 시작:

`redis-server --port {{포트}} --daemonize yes`

- 사용자 지정 구성 파일을 사용하여 Redis 서버 시작:

`redis-server {{경로/대상/redis.conf}}`

- 상세 로그를 출력하며 Redis 서버 시작:

`redis-server --loglevel {{warning|notice|verbose|debug}}`
