# suspend

> 현재 쉘의 실행을 일시 중지.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-suspend>.

- 현재 쉘 일시 중지 (`su`와 같이 중첩된 쉘에서 유용):

`{{bash}} <Enter> suspend`

- 중첩되지 않은 쉘에서 `suspend`를 사용한 경우, 별도의 터미널에서 실행을 재개:

`pkill -CONT {{bash}}`

- 시스템에 다시 접근할 수 없게 될 수 있는 경우에도, 강제로 쉘 일시 중지:

`suspend -f`
