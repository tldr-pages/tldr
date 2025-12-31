# printenv

> 모든 환경 변수 또는 지정된 환경 변수의 값을 출력.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/printenv-invocation.html>.

- 모든 환경 변수의 키-값 쌍 출력:

`printenv`

- 특정 변수의 값 출력:

`printenv {{HOME}}`

- 변수를 출력하고 줄바꿈 대신 NUL로 끝내기:

`printenv {{[-0|--null]}} {{HOME}}`
