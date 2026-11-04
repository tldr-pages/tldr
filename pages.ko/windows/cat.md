# cat

> PowerShell에서는, 원래의 `cat` 프로그램(`coreutils`의 일부)이 올바르게 설치되어 있지 않은 경우, 이 명령어는 `Get-Content`의 별칭일 수 있음.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-content>.

- 원래 `cat` 명령의 문서 보기:

`tldr cat {{[-p|--platform]}} common`

- PowerShell `Get-Content` 명령 문서 보기:

`tldr get-content`

- `cat`이 올바르게 설치되어 있는지 버전 정보를 출력하여 확인. 오류가 발생하면, PowerShell이 `Get-Content`로 대체했을 수 있음:

`cat --version`
