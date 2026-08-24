# zle

> Zsh Line Editor(ZLE) 위젯을 관리하는 도구.
> 참고: 일부 작업은 ZLE가 활성화된 상태(보통 사용자 정의 위젯 내부)에서만 사용할 수 있음.
> 관련 항목: `bindkey`.
> 더 많은 정보: <https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Zle-Builtins>.

- 사용자 정의 위젯 목록 출력([l]ist):

`zle -l`

- 내장 위젯을 포함한 모든 위젯 목록 출력([l]ist [a]ll):

`zle -la`

- 새로운([N]ew) 사용자 정의 위젯 생성 (기본 함수 이름은 위젯 이름과 동일):

`zle -N {{위젯_이름}} {{optional_shell_function_name}}`

- 위젯 삭제([D]elete):

`zle -D {{위젯_이름}}`

- 위젯 별칭([A]lias) 생성:

`zle -A {{original_widget}} {{별칭_이름}}`

- 다른 위젯 함수 내부에서 위젯 호출 (ZLE 활성 상태 필요):

`zle {{위젯_이름}}`

- 입력된 것처럼 텍스트를 ZLE 입력 큐에 추가 (ZLE 활성 상태 필요):

`zle -U "{{텍스트}}"`
