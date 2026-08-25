# function

> 함수 정의.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Shell-Functions>.

- 지정한 이름으로 함수 정의:

`function {{함수_이름}} { {{echo "Function contents here"}}; }`

- `func_name`이라는 함수 실행:

`func_name`

- `function` 키워드 없이 함수 정의:

`{{func_name}}() { {{echo "Function contents here"}}; }`

- 도움말 표시:

`help function`
