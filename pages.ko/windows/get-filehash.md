# Get-FileHash

> 파일의 해시를 계산.
> 참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>.

- SHA256 알고리즘을 사용하여 지정된 파일의 해시 계산:

`Get-FileHash {{경로\대상\파일}}`

- 지정된 알고리즘을 사용하여 지정된 파일의 해시 계산:

`Get-FileHash {{경로\대상\파일}} -Algorithm {{SHA1|SHA384|SHA256|SHA512|MD5}}`
