# cmd

> Windows 명령 인터프리터.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- 대화형 셸 세션 시작:

`cmd`

- 특정 [c]ommands 실행:

`cmd /c {{echo Hello world}}`

- 특정 스크립트 실행:

`cmd {{경로\대상\script.bat}}`

- 특정 명령을 실행한 후 대화형 셸로 진입:

`cmd /k {{echo Hello world}}`

- 명령 출력에서 `echo`가 비활성화된 대화형 셸 세션 시작:

`cmd /q`

- 지연된 [v]ariable 확장이 활성화 또는 비활성화된 대화형 셸 세션 시작:

`cmd /v:{{on|off}}`

- 명령 [e]xtensions가 활성화 또는 비활성화된 대화형 셸 세션 시작:

`cmd /e:{{on|off}}`

- [u]nicode 인코딩을 사용하는 대화형 셸 세션 시작:

`cmd /u`
