# pg_test_timing

> 시스템의 타이밍 오버헤드를 측정하여 클록 단조성(ensure clock monotonicity)을 확인.
> 더 많은 정보: <https://www.postgresql.org/docs/current/pgtesttiming.html>.

- 기본 타이밍 테스트 실행 (3초):

`pg_test_timing`

- 사용자 지정 시간 동안 타이밍 테스트 실행:

`pg_test_timing {{[-d|--duration]}} {{초}}`
