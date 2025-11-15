# Get-WUSettings

> 현재 Windows Update 에이전트 구성을 가져옵니다. 외부 `PSWindowsUpdate` 모듈의 일부입니다.
> 이 명령은 PowerShell에서만 실행할 수 있습니다.
> 더 많은 정보: <https://github.com/mgajda83/PSWindowsUpdate>.

- 현재 Windows Update 에이전트 구성 가져오기:

`Get-WUSettings`

- 현재 구성 데이터를 이메일(SMTP)로 전송:

`Get-WUSettings -SendReport -PSWUSettings @{SmtpServer="{{smtp_서버}}"; Port={{smtp_포트}} From="{{이메일_보낸이}}" To="{{이메일_받는이}}"}`
