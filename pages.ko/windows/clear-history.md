# Clear-History

> PowerShell 세션 명령 기록을 삭제함.
> 참고: `clhy`는 `Clear-History`의 별칭으로 사용할 수 있음.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/clear-history>.

- 현재 세션의 모든 명령 기록 삭제:

`Clear-History`

- 지정한 명령의 기록 삭제:

`Clear-History -CommandLine "{{명령어}}"`

- 여러 명령의 기록 삭제:

`Clear-History -CommandLine {{"명령어1", "명령어2", ...}}`

- 지정한 ID의 기록 삭제:

`Clear-History -Id {{아이디_숫자}}`

- 여러 ID의 기록 삭제:

`Clear-History -Id {{아이디1, 아이디2, ...}}`

- 지정한 ID 범위의 기록 삭제:

`Clear-History -Id ({{시작_아이디}}..{{종료_아이디}})`

- 삭제될 항목만 표시:

`Clear-History -WhatIf`

- 삭제 전에 확인 메시지 표시:

`Clear-History -Confirm`
