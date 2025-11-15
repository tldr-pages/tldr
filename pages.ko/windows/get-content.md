# Get-Content

> 지정된 위치에 있는 항목의 내용을 가져옵니다.
> 참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-content>.

- 파일의 내용 표시:

`Get-Content -Path {{경로\대상\파일}}`

- 파일의 처음 몇 줄 표시:

`Get-Content -Path {{경로\대상\파일}} -TotalCount {{10}}`

- 파일의 내용을 표시하고 `<Ctrl c>`를 누를 때까지 계속 읽기:

`Get-Content -Path {{경로\대상\파일}} -Wait`
