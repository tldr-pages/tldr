# Out-GridView

> 명령 출력과 객체를 스크롤 및 검색이 가능한 대화형 GUI 창에 표시함.
> PowerShell 객체의 열을 자동으로 분석해, `stdout`을 대화형으로 필터링한 뒤 `stdin`으로 전달 가능.
> 참고: 이 명령은 Windows PowerShell에서만 사용 가능.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/out-gridview>.

- 명령 또는 cmdlet 출력을 새로운 창에 표시:

`{{command}} | Out-GridView`

- PowerShell 해시 테이블 (예: `$PSVersionTable`)을 표시하고 창이 닫힐 때까지 명령 대기:

`$PSVersionTable | Out-GridView -Wait`

- CSV 파일을 읽어 지정한 제목의 새 창에 표시:

`Import-Csv {{경로\대상\파일.csv}} | Out-GridView -Title "{{제목}}"`

- 이전 명령의 `stdout`에서 행을 대화형으로 선택하여 다음 명령의 `stdin`으로 전달 (다중 선택은 `<Ctrl LeftClick>`, `<Shift LeftClick>`, `<Shift ArrowUp>`, 또는 `<Shift ArrowDown>`을 사용):

`{{이전_명령어}} | Out-GridView -PassThru | {{새로운_명령어}}`

- 텍스트 파일의 행을 대화형으로 선택하여 다른 명령의 입력으로 전달:

`Get-Content {{경로\대상\파일.txt}} | Out-GridView -PassThru | {{명령어}}`
