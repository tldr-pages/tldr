# utmpdump

> btmp, utmp 및 wtmp 회계 파일을 덤프하고 로드합니다.
> 더 많은 정보: <https://manned.org/utmpdump>.

- `/var/log/wtmp` 파일을 일반 텍스트로 `stdout`에 덤프:

`utmpdump {{/var/log/wtmp}}`

- 이전에 덤프한 파일을 `/var/log/wtmp`에 로드:

`utmpdump -r {{덤프파일}} > {{/var/log/wtmp}}`
