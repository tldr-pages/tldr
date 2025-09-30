# Get-WUApiVersion

> Windows 업데이트 에이전트 버전을 확인합니다. 외부 `PSWindowsUpdate` 모듈의 일부입니다.
> 이 명령은 PowerShell에서만 실행할 수 있습니다.
> 더 많은 정보: <https://github.com/mgajda83/PSWindowsUpdate>.

- 현재 설치된 Windows 업데이트 에이전트 버전 확인:

`Get-WUApiVersion`

- 현재 설정 데이터를 이메일(SMTP)로 전송:

`Get-WUApiVersion -SendReport -PSWUSettings @{SmtpServer="{{smtp_서버}}"; Port={{smtp_포트}} From="{{이메일_보낸이}}" To="{{이메일_받는이}}"}`
