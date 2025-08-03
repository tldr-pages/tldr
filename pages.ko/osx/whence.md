# whence

> Zsh 내장 명령어로, 명령어가 어떻게 해석될지를 나타냅니다.
> 더 많은 정보: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html#index-whence>.

- `command`를 해석하고, `alias`로 정의된 경우 확장:

`whence "{{명령어}}"`

- `command`의 유형을 표시하고, 함수나 바이너리로 정의된 경우 위치도 함께 표시:

`whence -v "{{명령어}}"`

- 위와 동일하지만, 위치 대신 셸 함수의 내용을 표시:

`whence -c "{{명령어}}"`

- 위와 동일하지만, 명령어 경로상의 모든 발생을 표시:

`whence -ca "{{명령어}}"`

- `PATH`에서만 `command`를 검색하고, 내장 명령어, 별칭 또는 셸 함수를 무시:

`whence -p "{{명령어}}"`
