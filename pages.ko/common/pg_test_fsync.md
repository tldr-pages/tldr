# pg_test_fsync

> 시스템에서 가장 빠른 wal_sync_method를 확인.
> 더 많은 정보: <https://www.postgresql.org/docs/current/pgtestfsync.html>.

- 기본 fsync 성능 벤치마크 실행 (5초):

`pg_test_fsync`

- 사용자 지정 테스트 시간으로 벤치마크 실행:

`pg_test_fsync {{[-s|--secs-per-test]}} {{초}}`

- 지정한 파일 사용해 벤치마크 실행 (파일은 pg_wal 디렉터리와 동일한 파일 시스템에 있어야 함):

`pg_test_fsync {{[-f|--filename]}} {{경로/대상/파일}}`
