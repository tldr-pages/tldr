# PSVersionTable

> 현재 PowerShell 버전을 가져오는 읽기 전용 변수(`$PSVersionTable`)입니다.
> 이 명령은 PowerShell에서만 실행할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_automatic_variables#psversiontable>.

- 현재 설치된 PowerShell 버전 및 에디션 요약 출력:

`$PSVersionTable`

- PowerShell의 세부 버전 번호(주, 부, 빌드, 수정) 가져오기:

`$PSVersionTable.PSVersion`

- 이 PowerShell 버전이 지원하는 모든 PowerShell 스크립트 버전 나열:

`$PSVersionTable.PSCompatibleVersions`

- 현재 설치된 PowerShell 버전이 기반이 되는 최신 Git 커밋 ID 가져오기 (PowerShell 6.0 이상에서 작동):

`$PSVersionTable.GitCommitId`

- 사용자가 PowerShell Core (6.0 이상) 또는 원본 "Windows PowerShell" (버전 5.1 이하)을 실행하는지 확인:

`$PSVersionTable.PSEdition`
