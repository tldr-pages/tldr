# xdg-settings

> XDG 호환 데스크탑 환경의 설정 관리.
> 더 많은 정보: <https://portland.freedesktop.org/doc/xdg-settings.html>.

- 기본 웹 브라우저 출력:

`xdg-settings get {{기본-웹-브라우저}}`

- 기본 웹 브라우저를 Firefox로 설정:

`xdg-settings set {{기본-웹-브라우저}} {{firefox.desktop}}`

- 기본 메일 URL 스킴 핸들러를 Evolution으로 설정:

`xdg-settings set {{기본-url-스킴-핸들러}} {{mailto}} {{evolution.desktop}}`

- 기본 PDF 문서 뷰어 설정:

`xdg-settings set {{pdf-뷰어.desktop}}`

- 도움말 표시:

`xdg-settings --help`
