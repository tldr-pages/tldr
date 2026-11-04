# return

> 함수 종료.
> `source`로 실행된 스크립트에서는 스크립트를 종료할 수도 있음.
> 관련 항목: `exit`.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-return>.

- 함수를 중간에 즉시 종료:

`{{함수_이름}}() { {{echo "This is reached"}}; return; {{echo "This is not"}}; }`

- 함수의 반환 상태 코드 지정:

`{{함수_이름}}() { return {{종료 코드}}; }`
