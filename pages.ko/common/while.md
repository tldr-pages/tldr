# while

> 간단한 셸 루프.
> 더 많은 정보: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_04_09>.

- `stdin`을 읽고 각 줄에 대해 작업 수행:

`while read line; do echo "$line"; done`

- 매초마다 명령을 영구적으로 실행:

`while :; do {{명령}}; sleep 1; done`
