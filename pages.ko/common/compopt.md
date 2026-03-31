# compopt

> 명령어 자동완성 옵션을 출력하거나 변경.
> `-o`는 활성화, `+o`는 비활성화를 의미.
> 관련 항목: `compgen`, `complete`.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-compopt>.

- 지정한 명령의 자동완성 옵션을 표시:

`compopt {{명령어}}`

- 명령의 자동완성 옵션을 활성화하거나 비활성화:

`compopt {{-o|+o}} {{option1}} {{-o|+o}} {{option2}} {{명령어}}`

- 현재 실행 중인 자동완성의 옵션을 표시:

`compopt`

- 현재 명령의 자동완성 옵션을 활성화하거나 비활성화:

`compopt {{-o|+o}} {{옵션1}} {{-o|+o}} {{옵션2}}`
