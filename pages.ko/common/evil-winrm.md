# evil-winrm

> 침투 테스트를 위한 WinRM(Windows 원격 관리 쉘).
> 연결되면, 대상 호스트에 PowerShell 프롬프트가 표시됨.
> 더 많은 정보: <https://github.com/Hackplayers/evil-winrm>.

- 호스트에 연결:

`evil-winrm --ip {{아이피}} --user {{사용자}} --password {{비밀번호}}`

- 비밀번호 해시를 전달하여 호스트에 연결:

`evil-winrm --ip {{아이피}} --user {{사용자}} --hash {{nt_hash}}`

- 스크립트 및 실행 파일에 대한 디렉터리를 지정하여 호스트에 연결:

`evil-winrm --ip {{아이피}} --user {{사용자}} --password {{비밀번호}} --scripts {{경로/대상/스크립트}} --executables {{경로/대상/실행파일}}`

- SSL을 사용하여 호스트에 연결:

`evil-winrm --ip {{아이피}} --user {{사용자}} --password {{비밀번호}} --ssl --pub-key {{경로/대상/공개키}} --priv-key {{경로/대상/개인키}}`

- 호스트에 파일 업로드:

`PS > upload {{경로/대상/로컬/파일}} {{경로/대상/원격/파일}}`

- 로드된 모든 PowerShell 함수를 나열:

`PS > menu`

- `--scripts` 디렉터리에서 PowerShell 스크립트를 로드:

`PS > {{스크립트.ps1}}`

- `--executables` 디렉터리에서 호스트의 바이너리를 호출:

`PS > Invoke-Binary {{바이너리.exe}}`
