# Set-Acl

> 지정된 항목(예: 파일 또는 레지스트리 키)의 보안 설명자를 변경합니다.
> 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/set-acl>.

- 하나의 파일에서 보안 설명자를 복사하여 다른 파일에 적용:

`$OriginAcl = Get-Acl -Path {{경로\대상\파일}}; Set-Acl -Path {{경로\대상\파일}} -AclObject $OriginAcl`

- 파이프라인 연산자를 사용하여 설명자 전달:

`Get-Acl -Path {{경로\대상\파일}} | Set-Acl -Path {{경로\대상\파일}}`
