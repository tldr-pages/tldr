# dpkg-query

> 설치된 패키지에 대한 정보 표시.
> 더 많은 정보: <https://manned.org/dpkg-query.1>.

- 설치된 모든 패키지 나열:

`dpkg-query --list`

- 패턴과 일치하는 설치된 패키지 나열:

`dpkg-query --list '{{libc6*}}'`

- 패키지에 의해 설치된 모든 파일 나열:

`dpkg-query --listfiles {{libc6}}`

- 패키지에 대한 정보 표시:

`dpkg-query --status {{libc6}}`

- 패턴과 일치하는 파일을 소유한 패키지 검색:

`dpkg-query --search {{/etc/ld.so.conf.d}}`
