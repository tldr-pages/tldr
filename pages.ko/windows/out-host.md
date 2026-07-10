# Out-Host

> PowerShell 세션에서 명령의 `stdout`을 처리하여 출력.
> `more` 명령의 대체 용도로도 사용 가능.
> 참고: 이 명령은 PowerShell에서만 사용 가능.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/out-host>.

- 명령의 출력 또는 변수 값을 명령 줄에 표시 ( `Out-Host` 없이 실행한 것과 동일):

`{{명령어_또는_변수}} | Out-Host`

- 출력을 대화형 페이지 보기(Paging View)로 표시 (PowerShell ISE에서는 지원되지 않음):

`{{명령어_또는_변수}} | Out-Host -Paging`

- 텍스트 파일을 대화형 페이지 보기로 표시 (`more path/to/file`과 동일):

`Get-Content {{경로\대상\파일}} | Out-Host -Paging`

- 페이지 보기에서 다음 페이지로 이동:

`<Space>`

- 페이지 보기에서 다음 줄로 이동:

`<Enter>`

- 페이지 보기 종료:

`<q>`
