# more

> `stdin` 또는 파일에서 페이지 단위 출력을 표시합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- `stdin`에서 페이지 단위 출력 표시:

`{{echo test}} | more`

- 하나 이상의 파일에서 페이지 단위 출력 표시:

`more {{경로\대상\파일}}`

- 탭을 지정된 수의 공백으로 변환:

`more {{경로\대상\파일}} /t{{공백}}`

- 페이지 표시 전에 화면 지우기:

`more {{경로\대상\파일}} /c`

- 출력을 5번째 줄에서 시작:

`more {{경로\대상\파일}} +{{5}}`

- 확장된 대화형 모드 활성화 (사용법 보기):

`more {{경로\대상\파일}} /e`

- 도움말 표시:

`more /?`
