# Get-WUHistory

> Windows Update에서 설치된 업데이트의 기록을 가져옵니다. 외부 `PSWindowsUpdate` 모듈의 일부입니다.
> 이 명령은 PowerShell에서만 실행할 수 있습니다.
> 더 많은 정보: <https://github.com/mgajda83/PSWindowsUpdate>.

- 업데이트 기록 목록 가져오기:

`Get-WUHistory`

- 최근 10개의 설치된 업데이트 나열:

`Get-WUHistory -Last {{10}}`

- 특정 날짜부터 오늘까지 설치된 모든 업데이트 나열:

`Get-WUHistory -MaxDate {{날짜}}`

- 지난 24시간 동안 설치된 모든 업데이트 나열:

`Get-WUHistory -MaxDate (Get-Date).AddDays(-1)`

- 결과를 이메일(SMTP)로 전송:

`Get-WUHistory -SendReport -PSWUSettings @{SmtpServer="{{smtp_서버}}"; Port={{smtp_포트}} From="{{발신자_이메일}}" To="{{수신자_이메일}}"}`
