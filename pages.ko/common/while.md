# while

> 간단한 셸 루프.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-while>.

- `stdin`을 읽고 각 줄에 대해 작업 수행:

`while read line; do echo "$line"; done`

- 매초마다 명령을 영구적으로 실행:

`while :; do {{명령}}; sleep 1; done`
