# break

> `for`, `while`, `until`, `select` 루프에서 빠져나오기.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-break>.

- 하나의 루프에서 빠져나오기:

`while :; do break; done`

- 중첩된 루프에서 빠져나오기:

`while :; do while :; do break 2; done; done`
