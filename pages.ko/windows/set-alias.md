# Set-Alias

> PowerShell에서 별칭을 설정하거나 수정하는 명령어.
> 참고: `sal`은 `Set-Alias`의 별칭으로 사용할 수 있음.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/set-alias>.

- 새로운 별칭 생성 또는 재할당:

`Set-Alias -Name {{텍스트}} -Value {{명령어}}`

- 별칭에 설명 추가:

`Set-Alias -Name {{텍스트}} -Value {{명령어}} -Description "{{설명}}"`
