# taskkill

> 프로세스 아이디 또는 이름으로 프로세스를 종료합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/taskkill>.

- 프로세스 아이디로 프로세스 종료:

`taskkill /pid {{프로세스_아이디}}`

- 프로세스 이름으로 프로세스 종료:

`taskkill /im {{프로세스_이름}}`

- 강제로 지정된 프로세스 종료:

`taskkill /pid {{프로세스_아이디}} /f`

- 프로세스 및 자식 프로세스 종료:

`taskkill /im {{프로세스_이름}} /t`

- 원격 머신에서 프로세스 종료:

`taskkill /pid {{프로세스_아이디}} /s {{원격_이름}}`

- 명령어 사용 정보 표시:

`taskkill /?`
