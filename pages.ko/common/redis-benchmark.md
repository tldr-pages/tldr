# redis-benchmark

> Redis 서버의 성능을 테스트.
> 더 많은 정보: <https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/>.

- 전체 벤치마크 실행:

`redis-benchmark`

- 특정 Redis 서버에서 벤치마크 실행:

`redis-benchmark -h {{호스트}} -p {{포트}} -a {{비밀번호}}`

- 기본 100000 요청으로 테스트의 일부 실행:

`redis-benchmark -h {{호스트}} -p {{포트}} -t {{set,lpush}} -n {{100000}}`

- 특정 스크립트로 실행:

`redis-benchmark -n {{100000}} script load "{{redis.call('set', 'foo', 'bar')}}"`

- 100000개의 [r]andom 키를 사용하여 벤치마크 실행:

`redis-benchmark -t {{set}} -r {{100000}}`

- 16개의 명령으로 [P]ipelining하여 벤치마크 실행:

`redis-benchmark -n {{1000000}} -t {{set,get}} -P {{16}}`

- [q]uietly 실행하여 초당 쿼리 결과만 표시:

`redis-benchmark -q`
