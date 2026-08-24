# bindkey

> Z 셸에 단축키를 추가합니다.
> 관련 항목: `zle`.
> 더 많은 정보: <https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Zle-Builtins>.

- 등록된 단축키 목록을 표시:

`bindkey`

- 특정 명령에 단축키를 바인딩:

`bindkey "{{^k}}" {{kill-line}}`

- 핫키를 특정 키 시퀀스([s]equence)에 바인딩:

`bindkey -s '^o' 'cd ..\n'`

- 키맵의 목록([l]ist)을 출력:

`bindkey -l`

- 키맵(key[M]ap)에서 단축키 보기:

`bindkey -M {{main}}`

- [v]i 모드를 활성화:

`bindkey -v`

- [e]macs 모드를 활성화 (기본 모드):

`bindkey -e`

- 어떤 모드가 활성화되어 있는지 확인 (vi 또는 emacs):

`bindkey -lL main | grep -Eo 'viins|emacs'`
