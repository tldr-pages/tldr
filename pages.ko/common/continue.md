# continue

> `for`, `while`, `until`, 또는 `select` 루프에서 다음 반복으로 건너뜀.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-continue>.

- 다음 반복으로 건너뛰기:

`while :; do continue; {{echo "This will never be reached"}}; done`

- 중첩된 루프에서 바깥 루프의 다음 반복으로 건너뛰기:

`for i in {{{1..3}}}; do {{echo $i}}; while :; do continue 2; done; done`
