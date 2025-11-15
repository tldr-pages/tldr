# dmesg

> 커널 메시지를 `stdout`에 출력.
> 더 많은 정보: <https://manned.org/dmesg>.

- 커널 메시지 표시:

`sudo dmesg`

- 커널 오류 메시지 표시:

`sudo dmesg {{[-l|--level]}} err`

- 커널 메시지를 표시하고 새로운 메시지를 계속 읽기 (`tail -f`와 유사, 커널 3.5.0 이상에서 사용 가능):

`sudo dmesg {{[-w|--follow]}}`

- 이 시스템에서 사용 가능한 물리적 메모리 용량 표시:

`sudo dmesg | grep {{[-i|--ignore-case]}} memory`

- 한 페이지씩 커널 메시지 표시:

`sudo dmesg | less`

- 타임스탬프와 함께 커널 메시지 표시 (커널 3.5.0 이상에서 사용 가능):

`sudo dmesg {{[-T|--ctime]}}`

- 사람이 읽기 쉬운 형식으로 커널 메시지 표시 (커널 3.5.0 이상에서 사용 가능):

`sudo dmesg {{[-H|--human]}}`

- 출력에 색상 적용 (커널 3.5.0 이상에서 사용 가능):

`sudo dmesg {{[-L|--color]}}`
