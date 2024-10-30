# setx

> 영구적인 환경 변수를 설정합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/setx>.

- 현재 사용자에 대한 환경 변수 설정:

`setx {{변수}} {{값}}`

- 현재 컴퓨터에 대한 환경 변수 설정:

`setx {{변수}} {{값}} /M`

- 원격 컴퓨터의 사용자에 대한 환경 변수 설정:

`setx /s {{호스트명}} /u {{사용자명}} /p {{암호}} {{변수}} {{값}}`

- 레지스트리 키 값에서 환경 변수 설정:

`setx {{변수}} /k {{레지스트리\키\경로}}`
