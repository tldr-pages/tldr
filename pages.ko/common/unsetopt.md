# unsetopt

> Z 쉘 (`zsh`)의 옵션을 해제.
> 참고: Zsh 옵션은 대소문자를 구분하지 않으며 밑줄은 무시됨.
> 관련 항목: `setopt`.
> 더 많은 정보: <https://zsh.sourceforge.io/Doc/Release/Options.html>.

- 현재 해제된 모든 옵션 목록 표시 (`setopt`으로 설정된 옵션 목록 확인 가능):

`unsetopt`

- 지정한 옵션 해제:

`unsetopt {{옵션_이름}}`

- 여러 옵션을 한 번에 해제:

`unsetopt {{옵션_이름1 옵션_이름2 ...}}`
