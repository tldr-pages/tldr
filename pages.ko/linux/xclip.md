# xclip

> X11 클립보드 조작 도구로, `xsel`과 유사합니다.
> X 기본 및 보조 선택 영역과 시스템 클립보드(`<Ctrl c>`/`<Ctrl v>`)를 처리합니다.
> 관련 항목: `wl-copy`.
> 더 많은 정보: <https://manned.org/xclip>.

- 명령의 출력을 X11 기본 선택 영역(클립보드)에 복사:

`echo 123 | xclip`

- 명령의 출력을 지정된 X11 선택 영역에 복사:

`echo 123 | xclip {{[-se|-selection]}} {{primary|secondary|clipboard}}`

- 명령의 출력을 시스템 클립보드에 짧은 표기법을 사용하여 복사:

`echo 123 | xclip {{[-se|-selection]}} {{[c|clipboard]}}`

- 파일의 내용을 시스템 클립보드에 복사:

`xclip {{[-se|-selection]}} {{[c|clipboard]}} {{입력_파일.txt}}`

- PNG 파일의 내용을 시스템 클립보드에 복사 (다른 프로그램에 올바르게 붙여넣기 가능):

`xclip {{[-se|-selection]}} {{[c|clipboard]}} {{[-t|-target]}} image/png {{입력_파일.png}}`

- 콘솔에서 사용자 입력을 시스템 클립보드에 복사:

`xclip {{[-i|-in]}}`

- X11 기본 선택 영역의 내용을 콘솔에 붙여넣기:

`xclip {{[-o|-out]}}`

- 시스템 클립보드의 내용을 콘솔에 붙여넣기:

`xclip {{[-o|-out]}} {{[-se|-selection]}} {{[c|clipboard]}}`
