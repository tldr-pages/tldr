# seq

> 숫자 시퀀스를 `stdout`에 출력.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/seq-invocation.html>.

- 1부터 10까지의 시퀀스:

`seq 10`

- 5부터 20까지 3씩 증가하는 숫자:

`seq 5 3 20`

- 출력 항목을 줄바꿈 대신 공백으로 구분:

`seq {{[-s|--separator]}} " " 5 3 20`

- 출력 너비를 최소 4자리로 맞추고 필요한 경우 0으로 채움:

`seq {{[-f|--format]}} "%04g" 5 3 20`
