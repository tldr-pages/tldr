# clip

> 입력 내용을 Windows 클립보드에 복사.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- 명령줄 출력 결과를 Windows 클립보드로 파이프:

`{{dir}} | clip`

- 파일의 내용을 Windows 클립보드에 복사:

`clip < {{경로\대상\파일.ext}}`

- 끝에 줄 바꿈이 있는 텍스트를 Windows 클립보드에 복사:

`echo {{일부 텍스트}} | clip`

- 끝에 줄 바꿈이 없는 텍스트를 Windows 클립보드에 복사:

`echo | set /p="some text" | clip`
