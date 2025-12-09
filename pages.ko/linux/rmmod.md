# rmmod

> Linux 커널에서 모듈을 제거합니다.
> 더 많은 정보: <https://manned.org/rmmod>.

- 커널에서 모듈 제거:

`sudo rmmod {{모듈_이름}}`

- 커널에서 모듈을 제거하고 자세한 정보 표시:

`sudo rmmod --verbose {{모듈_이름}}`

- 커널에서 모듈을 제거하고 오류를 `stderr` 대신 syslog로 전송:

`sudo rmmod --syslog {{모듈_이름}}`

- 도움말 표시:

`rmmod --help`

- 버전 표시:

`rmmod --version`
