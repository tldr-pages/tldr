# Start-Process

> 새로운 프로세스에서 명령 시작.
> `PATH` 환경 변수에 등록되지 않았더라도  Windows 레지스트리의 `App Paths`에 등록된 프로그램 실행할 수도 있음.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/start-process>.

- Windows 탐색기에서 지정한 디렉터리 열기 (`explorer 경로\대상\디렉터리`와 동일):

`Start-Process {{경로\대상\디렉터리}}`

- 지정한 Windows 프로그램 실행 (명령줄 프로그램은 새 콘솔 창에서 실행):

`Start-Process {{경로\대상\파일}}`

- 등록된 Windows 프로그램 이름으로 실행하고 명령줄 인수 전달:

`Start-Process {{msedge}} {{--inprivate example.com}}`

- 최소화 또는 최대화된 창으로 Windows 프로그램 실행:

`Start-Process -WindowStyle {{Minimized|Maximized}} {{프로그램}}`

- 지정한 작업 디렉터리에서 명령 또는 프로그램 실행:

`Start-Process -WorkingDirectory {{경로\대상\디렉터리}} {{명령_또는_프로그램}}`

- 대상 명령 또는 프로그램이 종료될 때까지 대기:

`Start-Process -Wait {{명령_또는_프로그램}}`
