# ulimit

> 사용자 제한을 조회하고 설정.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-ulimit>.

- 모든 사용자 제한의 속성 조회:

`ulimit -a`

- 동시에 열 수 있는 파일 개수의 하드 제한 조회:

`ulimit -H -n`

- 동시에 열 수 있는 파일 개수의 소프트 제한 조회:

`ulimit -S -n`

- 사용자별 프로세스 최대 개수 설정:

`ulimit -u 30`
