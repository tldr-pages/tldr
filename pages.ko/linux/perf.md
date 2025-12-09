# perf

> Linux 성능 카운터 측정을 위한 프레임워크.
> 더 많은 정보: <https://perfwiki.github.io/main/>.

- 명령에 대한 기본 성능 카운터 통계 표시:

`perf stat {{gcc hello.c}}`

- 시스템 전역의 실시간 성능 카운터 프로필 표시:

`sudo perf top`

- 명령을 실행하고 프로필을 `perf.data`에 기록:

`sudo perf record {{명령}}`

- 기존 프로세스의 프로필을 `perf.data`에 기록:

`sudo perf record -p {{pid}}`

- `perf.data`( `perf record`에 의해 생성됨)를 읽고 프로필 표시:

`sudo perf report`
