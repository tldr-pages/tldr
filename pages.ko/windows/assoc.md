# assoc

> 파일 확장자와 파일 유형 간의 연결을 표시하거나 변경.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/assoc>.

- 파일 확장자와 파일 유형 간의 모든 연결 나열:

`assoc`

- 특정 확장자의 연결된 파일 유형 표시:

`assoc {{.txt}}`

- 특정 확장자의 연결된 파일 유형 설정:

`assoc .{{txt}}={{txtfile}}`

- `assoc`의 출력을 한 화면씩 보기:

`assoc | {{more}}`
