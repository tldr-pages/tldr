# svcs

> 실행 중인 서비스에 대한 정보를 나열합니다.
> 더 많은 정보: <https://www.unix.com/man-page/linux/1/svcs>.

- 모든 실행 중인 서비스를 나열:

`svcs`

- 실행되고 있지 않은 서비스를 나열:

`svcs -vx`

- 서비스에 대한 정보를 나열:

`svcs apache`

- 서비스 로그 파일의 위치 표시:

`svcs -L apache`

- 서비스 로그 파일의 끝을 표시:

`tail $(svcs -L apache)`
