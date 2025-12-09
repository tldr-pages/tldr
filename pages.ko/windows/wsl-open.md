# wsl-open

> 사용자의 기본 Windows GUI 애플리케이션에서 Windows Subsystem for Linux 내에서 파일이나 URL을 엽니다.
> 더 많은 정보: <https://gitlab.com/4U6U57/wsl-open>.

- Windows 탐색기에서 현재 디렉토리 열기:

`wsl-open {{.}}`

- Windows에서 사용자의 기본 웹 브라우저에 URL 열기:

`wsl-open {{https://example.com}}`

- Windows에서 사용자의 기본 애플리케이션에 특정 파일 열기:

`wsl-open {{경로\파일}}`

- `wsl-open`을 쉘의 웹 브라우저로 설정 (링크를 `wsl-open`으로 열기):

`wsl-open -w`

- 도움말 표시:

`wsl-open -h`
