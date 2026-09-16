# sccache

> 빠른 C/C++/Rust 컴파일러 캐시.
> 클라이언트와 서버로 구성되며, 둘 다 로컬 시스템에서 실행됨.
> 더 많은 정보: <https://manned.org/sccache>.

- 컴파일 통계 표시:

`sccache {{[-s|--show-stats]}}`

- `sccache`를 통해 `gcc` (또는 다른 컴파일러 명령) 실행:

`sccache gcc {{경로/대상/파일.c}}`

- `sccache` 서버를 포그라운드에서 시작하고 로그를 출력:

`sccache --stop-server; SCCACHE_LOG=trace SCCACHE_START_SERVER=1 SCCACHE_NO_DAEMON=1 sccache`

- 스케줄러에 분산 컴파일 상태 요청:

`sccache --dist-status`
