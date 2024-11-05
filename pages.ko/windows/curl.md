# curl

> PowerShell에서는 원본 `curl` 프로그램(<https://curl.se>)이 제대로 설치되지 않은 경우 이 명령이 `Invoke-WebRequest`의 별칭일 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- 원본 `curl` 명령에 대한 문서 보기:

`tldr curl -p common`

- PowerShell의 `Invoke-WebRequest` 명령에 대한 문서 보기:

`tldr invoke-webrequest`

- `curl`이 제대로 설치되었는지 버전 번호를 출력하여 확인. 이 명령이 오류로 평가된다면, PowerShell이 이 명령을 `Invoke-WebRequest`로 대체했을 수 있습니다:

`curl --version`
