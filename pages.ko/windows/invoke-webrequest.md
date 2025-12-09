# Invoke-WebRequest

> HTTP/HTTPS 요청을 수행합니다.
> 참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- URL의 내용을 파일로 다운로드:

`Invoke-WebRequest {{http://example.com}} -OutFile {{경로\대상\파일}}`

- 폼 인코딩된 데이터 전송(`application/x-www-form-urlencoded` 타입의 POST 요청):

`Invoke-WebRequest -Method Post -Body @{ name='bob' } {{http://example.com/form}}`

- 사용자 정의 HTTP 메서드 사용하여 추가 헤더가 있는 요청 전송:

`Invoke-WebRequest -Headers {{@{ X-My-Header = '123' }}} -Method {{PUT}} {{http://example.com}}`

- 적절한 content-type 헤더 지정하여 JSON 형식의 데이터 전송:

`Invoke-WebRequest -Body {{'{"name":"bob"}'}} -ContentType 'application/json' {{http://example.com/users/1234}}`

- 서버 인증을 위한 사용자 이름과 비밀번호 전달:

`Invoke-WebRequest -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("myusername:mypassword")) } {{http://example.com}}`
