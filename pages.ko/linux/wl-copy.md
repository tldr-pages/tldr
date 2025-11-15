# wl-copy

> Wayland 클립보드에 복사 및 지우기.
> 같이 보기: `wl-paste`, `xclip`.
> 더 많은 정보: <https://github.com/bugaevc/wl-clipboard>.

- 텍스트를 클립보드에 복사:

`wl-copy "{{텍스트}}"`

- 명령어 (`ls`) 출력을 파이프로 클립보드에 복사:

`{{ls}} | wl-copy`

- 한 번만 붙여넣기 후 클립보드를 지우기:

`wl-copy --paste-once "{{텍스트}}"`

- 이미지를 복사:

`wl-copy < {{경로/대상/이미지}}`

- 클립보드 지우기:

`wl-copy --clear`
