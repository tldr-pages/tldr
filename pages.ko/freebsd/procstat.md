# procstat

> FreeBSD에서 프로세스에 대한 상세 정보를 표시하는 도구.
> 더 많은 정보: <https://man.freebsd.org/cgi/man.cgi?procstat>.

- 특정 프로세스의 파일 디스크립터 출력:

`procstat fds {{pid}}`

- 프로세스의 가상 메모리 매핑 정보 출력:

`procstat vm {{pid}}`

- 프로세스 인자 출력:

`procstat arguments {{pid}}`

- 프로세스의 리소스 제한 정보 출력:

`procstat rlimit {{pid}}`
