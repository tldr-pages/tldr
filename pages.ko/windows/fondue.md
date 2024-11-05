# fondue

> 선택적 Windows 기능 설치.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/fondue>.

- 특정 Windows 기능 활성화:

`fondue /enable-feature:{{기능}}`

- 사용자에게 모든 출력 메시지 숨기기:

`fondue /enable-feature:{{기능}} /hide-ux:all`

- 오류 보고를 위한 호출자 프로세스 이름 지정:

`fondue /enable-feature:{{기능}} /caller-name:{{이름}}`
