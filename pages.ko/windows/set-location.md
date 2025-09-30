# Set-Location

> 현재 작업 디렉토리를 표시하거나 다른 디렉토리로 이동합니다.
> 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- 지정된 디렉토리로 이동:

`Set-Location {{경로\대상\폴더}}`

- 다른 드라이브의 특정 디렉토리로 이동:

`Set-Location {{C}}:{{경로\대상\폴더}}`

- 지정된 디렉토리의 위치 표시:

`Set-Location {{경로\대상\폴더}} -PassThru`

- 현재 디렉토리의 상위 디렉토리로 이동:

`Set-Location ..`

- 현재 사용자의 홈 디렉토리로 이동:

`Set-Location ~`

- 이전에 선택한 디렉토리로 돌아가기/앞으로 이동:

`Set-Location {{-|+}}`

- 현재 드라이브의 루트 디렉토리로 이동:

`Set-Location \`
