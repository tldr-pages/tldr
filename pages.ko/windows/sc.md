# sc

> Service Control Manager 및 서비스와 통신합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/sc-query>.

- 서비스 상태 표시 (서비스 이름이 없으면 모든 서비스 표시):

`sc.exe query {{서비스명}}`

- 서비스 비동기적으로 시작:

`sc.exe create {{서비스명}} binpath= {{경로\대상\서비스_이진_파일}}`

- 서비스 비동기적으로 중지:

`sc.exe delete {{서비스명}}`

- 서비스 유형 설정:

`sc.exe config {{서비스명}} type= {{서비스_유형}}`
