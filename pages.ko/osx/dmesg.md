# dmesg

> 커널 메시지를 `stdout`에 출력합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/dmesg.8.html>.

- 커널 메시지 표시:

`dmesg`

- 이 시스템에서 사용 가능한 물리적 메모리 양 표시:

`dmesg | grep -i memory`

- 한 번에 한 페이지씩 커널 메시지 표시:

`dmesg | less`
