# unset

> 셸 변수 또는 함수를 제거.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-unset>.

- 변수 `foo`를 제거하거나, 변수가 존재하지 않을 경우 함수 `foo`를 제거:

`unset {{foo}}`

- 변수 `foo`와 `bar` 제거:

`unset -v {{foo}} {{bar}}`

- 함수 `my_func` 제거:

`unset -f {{my_func}}`
