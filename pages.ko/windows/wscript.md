# wscript

> 그래픽 사용자 인터페이스 (GUI)에서 Windows Script Host 프로그램을 실행.
> 관련 항목: 명령줄 인터페이스 (CLI)용은 `cscript`를 함께 참고.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/cscript>.

- Windows Script Host 프로그램의 기본 인터프리터를 `cscript` (CLI) 또는 `wscript` (GUI)로 설정:

`wscript //h:{{cscript|wscript}}`

- 스크립트 실행:

`wscript {{경로\대상\스크립트.vbs}}`

- 대화형([i]nteractive) 모드 또는 배치([b]atch) 모드로 스크립트 실행 (알림, 프롬프트 및 스크립트 오류 표시 또는 숨김):

`wscript //{{i|b}} {{경로\대상\스크립트.vbs}}`

- 실행 전에 Windows Script Host 로고 표시 또는 숨김 (Host 버전 확인 또는 출력 숨김에 유용):

`wscript {{//logo|//nologo}} {{경로\대상\스크립트.vbs}}`

- 사용자 지정 실행 엔진을 사용하여 스크립트 실행 (사용자 지정 스크립트 파일 확장자 사용 시 유용):

`wscript //e:{{jscript|vbscript|custom_engine}} {{경로\대상\스크립트.vbs}}`

- 스크립트 실행 제한 시간(초)([t]imeout) 설정:

`wscript //t:{{초}} {{경로\대상\스크립트.vbs}}`

- 디버거([d]ebugger)를 시작하고 스크립트 오류가 발생할 때까지 대기:

`wscript //d {{경로\대상\스크립트.vbs}}`

- IDE(예: Visual Studio)에서 첫 번째 스크립트 줄부터 디버깅 시작:

`wscript //x {{경로\대상\스크립트.vbs}}`
