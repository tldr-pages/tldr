# doskey

> 매크로, Windows 명령 및 명령줄을 관리합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/doskey>.

- 사용 가능한 매크로 나열:

`doskey /macros`

- 새 매크로 생성:

`doskey {{이름}} = "{{명령}}"`

- 특정 실행 파일에 대한 새 매크로 생성:

`doskey /exename={{실행파일}} {{이름}} = "{{명령}}"`

- 매크로 제거:

`doskey {{이름}} =`

- 메모리에 저장된 모든 명령 표시:

`doskey /history`

- 매크로를 파일에 저장하여 휴대성 확보:

`doskey /macros > {{경로\대상\macinit_파일}}`

- 파일에서 매크로 로드:

`doskey /macrofile = {{경로\대상\macinit_파일}}`
