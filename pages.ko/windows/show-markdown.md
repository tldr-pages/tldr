# Show-Markdown

> VT100 이스케이프 시퀀스를 사용하거나 HTML을 사용하는 브라우저에서 친숙한 방법으로 콘솔의 Markdown 파일 또는 문자열을 표시합니다.
> 참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/show-markdown>.

- 파일에서 콘솔로 Markdown 렌더링:

`Show-Markdown -Path {{경로\대상\파일}}`

- 문자열에서 콘솔로 Markdown 렌더링:

`"{{# Markdown content}}" | Show-Markdown`

- 브라우저에서 Markdown 파일 열기:

`Show-Markdown -Path {{경로\대상\파일}} -UseBrowser`
