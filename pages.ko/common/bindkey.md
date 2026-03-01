# bindkey

> Z-Shell에 키 바인딩을 추가.
> 관련 항목: `zle`.
> 더 많은 정보: <https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Zle-Builtins>.

- 특정 명령에 단축키를 바인딩:

`bindkey "{{^k}}" {{kill-line}}`

- 핫키를 특정 키 시퀀스([s]equence)에 바인딩:

`bindkey -s '^o' 'cd ..\n'`

- 키맵의 목록([l]ist)을 출력:

`bindkey -l`

- 키맵(key[M]ap)에서 단축키 보기:

`bindkey -M main`
