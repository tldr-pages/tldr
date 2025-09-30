# cd

> 현재 작업 중인 디렉토리를 표시하거나 다른 디렉토리로 이동.
> PowerShell에서는 이 명령이 `Set-Location`의 별칭입니다. 이 문서는 Command Prompt(`cmd`) 버전의 `cd`를 기반으로 합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- PowerShell의 동등한 명령에 대한 문서 보기:

`tldr set-location`

- 현재 디렉토리의 경로 표시:

`cd`

- 같은 드라이브의 특정 디렉토리로 이동:

`cd {{경로\대상\디렉토리}}`

- 다른 [d]rive의 특정 디렉토리로 이동:

`cd /d {{C}}:{{경로\대상\디렉토리}}`

- 현재 디렉토리의 상위 디렉토리로 이동:

`cd ..`

- 현재 사용자의 홈 디렉토리로 이동:

`cd %userprofile%`

- 현재 드라이브의 루트로 이동:

`cd \`
