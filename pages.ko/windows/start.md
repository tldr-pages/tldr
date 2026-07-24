# start

> 새 콘솔에서 명령을 시작.
> `PATH` 환경 변수에 등록되지 않았더라도  Windows 레지스트리의 `App Paths`에 등록된 프로그램 실행할 수도 있음.
> PowerShell에서는, 이 명령이 `Start-Process`의 별칭. 이 문서는 명령 프롬프트 (`cmd`)의 `start` 명령을 기준으로 함.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/start>.

- 해당하는 PowerShell 명령의 문서 보기:

`tldr start-process`

- 사용자 지정 창 제목으로 새 쉘 창 시작:

`start "{{창_제목}}" {{cmd|powershell|python|...}}`

- Windows 탐색기에서 지정한 디렉터리 열기 (`explorer 경로\대상\디렉터리`와 동일):

`start "" "{{경로\대상\디렉터리}}"`

- 지정한 Windows 프로그램 실행 (명령줄 프로그램은 새 콘솔 창에서 실행):

`start {{경로\대상\파일}}`

- 등록된 Windows 프로그램 이름으로 실행하고 명령줄 인수 전달:

`start {{msedge}} {{--inprivate example.com}}`

- 최소화 또는 최대화된 창으로 Windows 프로그램 실행:

`start {{/min|/max}} {{경로\대상\파일.exe}}`

- 지정한 작업 디렉터리에서 명령 또는 프로그램 실행:

`start /d {{경로\대상\디렉터리}} {{명령_또는_프로그램}}`

- 대상 명령 또는 프로그램이 종료될 때까지 대기:

`start /wait {{명령_또는_프로그램}}`
