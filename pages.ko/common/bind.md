# bind

> bash 단축키 및 변수를 관리하기 위한 bash 내장.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-bind>.

- 모든 바인딩된 명령어와 해당 단축키를 나열:

`bind {{-p|-P}}`

- 단축키에 대한 명령어를 쿼리:

`bind -q {{명령어}}`

- 키 바인딩:

`bind -x '"{{키_시퀸스}}":{{명령어}}'`

- 사용자 정의 바인딩 나열:

`bind -X`

- 도움말 표시:

`help bind`
