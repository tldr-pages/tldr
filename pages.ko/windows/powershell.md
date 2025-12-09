# powershell

> 시스템 관리를 위해 특별히 설계된 명령줄 쉘 및 스크립팅 언어입니다.
> 이 명령어는 PowerShell 버전 5.1 이하 (레거시 Windows PowerShell이라고도 함)를 참조합니다. 더 새로운, 크로스 플랫폼 버전의 PowerShell (PowerShell Core라고도 함)을 사용하려면 `pwsh` 대신 `powershell`을 사용하세요.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- 대화형 쉘 세션 시작:

`powershell`

- 시작 설정을 로드하지 않고 대화형 쉘 세션 시작:

`powershell -NoProfile`

- 특정 명령어 실행:

`powershell -Command "{{echo 'powershell is executed'}}"`

- 특정 스크립트 실행:

`powershell -File {{경로/대상/스크립트.ps1}}`

- 특정 버전의 PowerShell로 세션 시작:

`powershell -Version {{버전}}`

- 시작 명령을 실행한 후 쉘 종료 방지:

`powershell -NoExit`

- PowerShell에 전달되는 데이터의 형식 설명:

`powershell -InputFormat {{Text|XML}}`

- PowerShell에서 출력되는 데이터의 형식 설명:

`powershell -OutputFormat {{Text|XML}}`
