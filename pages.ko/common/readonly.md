# readonly

> 읽기 전용 셸 변수를 설정합니다.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-readonly>.

- 읽기 전용 변수 설정:

`readonly {{변수_이름}}={{값}}`

- 변수 읽기 전용으로 표시:

`readonly {{기존_변수}}`

- 모든 읽기 전용 변수의 이름과 값을 `stdout`에 [p]rint:

`readonly -p`
