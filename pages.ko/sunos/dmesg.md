# dmesg

> 커널 메시지를 `stdout`에 기록합니다.
> 더 많은 정보: <https://www.unix.com/man-page/sunos/1m/dmesg>.

- 커널 메시지 표시:

`dmesg`

- 시스템에서 사용 가능한 물리적 메모리 양 표시:

`dmesg | grep -i memory`

- 한 번에 한 페이지씩 커널 메시지 표시:

`dmesg | less`
