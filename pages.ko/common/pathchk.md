# pathchk

> 경로명의 유효성과 이식성을 확인합니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/pathchk-invocation.html>.

- 현재 시스템에서 경로명의 유효성을 확인:

`pathchk {{경로1 경로2 ...}}`

- 더 넓은 범위의 POSIX 호환 시스템에서 경로명의 유효성을 확인:

`pathchk -p {{경로1 경로2 ...}}`

- 모든 POSIX 호환 시스템에서 경로명의 유효성을 확인:

`pathchk {{[-p -P|--portability]}} {{경로1 경로2 ...}}`

- 빈 경로나 선행 대시(-)만 확인:

`pathchk -P {{경로1 경로2 ...}}`
