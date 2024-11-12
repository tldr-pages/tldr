# set

> 현재 CMD 인스턴스에 대한 환경 변수를 표시하거나 설정합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/set>.

- 현재 모든 환경 변수 표시:

`set`

- 특정 값으로 환경 변수 설정:

`set {{이름}}={{값}}`

- 지정된 문자열로 시작하는 환경 변수 표시:

`set {{이름}}`

- 지정된 변수에 대해 사용자에게 값 입력 요청:

`set /p {{이름}}={{프롬프트_문자열}}`
