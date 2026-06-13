# Get-Acl

> 파일이나 레지스트리 키와 같은 리소스의 보안 설명자를 가져옵니다.
> 참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/get-acl>.

- 특정 디렉토리의 ACL 표시:

`Get-Acl {{경로\대상\폴더}}`

- 레지스트리 키의 ACL 가져오기:

`Get-Acl -Path {{HKLM:\System\CurrentControlSet\Control}} | Format-List`
