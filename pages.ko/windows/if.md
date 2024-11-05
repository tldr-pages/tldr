# if

> 배치 스크립트에서 조건부 처리를 수행합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/if>.

- 조건이 참이면 지정된 명령을 실행:

`if {{조건}} ({{echo 조건 is true}})`

- 조건이 거짓이면 지정된 명령을 실행:

`if not {{조건}} ({{echo 조건 is true}})`

- 조건이 참이면 첫 번째 지정된 명령을 실행하고, 거짓이면 두 번째 지정된 명령을 실행:

`if {{조건}} ({{echo 조건 is true}}) else ({{echo 조건 is false}})`

- `%errorlevel%`이 지정된 종료 코드보다 크거나 같은지 확인:

`if errorlevel {{2}} ({{echo 조건 is true}})`

- 두 문자열이 같은지 확인:

`if %{{변수}}% == {{문자열}} ({{echo 조건 is true}})`

- 대소문자를 구분하지 않고 두 문자열이 같은지 확인:

`if /i %{{변수}}% == {{문자열}} ({{echo 조건 is true}})`

- 파일이 존재하는지 확인:

`if exist {{경로\대상\파일}} ({{echo 조건 is true}})`
