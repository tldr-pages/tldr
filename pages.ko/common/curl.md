# curl

> 데이터를 서버에서 혹은 서버로 전송.
> HTTP, HTTPS, FTP, SCP 등 대부분의 프로토콜 지원.
> 더 많은 정보: <https://curl.se/docs/manpage.html>.

- HTTP GET 요청을 수행하고 내용을 `stdout`에 덤프:

`curl {{https://example.com}}`

- HTTP GET 요청을 수행하고, `3xx` 리디렉션을 따라가며(fo[L]low), 응답 헤더와 내용을 `stdout`에 덤프([D]ump):

`curl {{[-L|--location]}} {{[-D|--dump-header]}} - {{https://example.com}}`

- URL에 표시된 파일명으로 출력([O]utput)을 저장하고 파일을 다운로드:

`curl {{[-O|--remote-name]}} {{http://example.com/filename.zip}}`

- 폼으로 인코딩된 데이터([d]ata) 전송 (POST 요청의 타입, `application/x-www-form-urlencoded`). `stdin`으로 부터 읽으려면 `--data @file_name` 이나 `--data @'-'`를 사용:

`curl {{[-X|--request]}} POST {{[-d|--data]}} {{'name=bob'}} {{http://example.com/form}}`

- 추가 헤더를 포함하여 요청을 전송하고, 사용자 지정 HTTP 메소드를 사용한 후 프록시(pro[x]y)를 통해 전송하고 (예: BurpSuite), 신뢰할 수 없는 자체 서명 인증서를 무시:

`curl {{[-k|--insecure]}} {{[-x|--proxy]}} {{http://127.0.0.1:8080}} {{[-H|--header]}} {{'Authorization: Bearer token'}} {{[-X|--request]}} {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- 적절한 컨텐츠 유형 헤더([H]eader)를 지정하여 JSON 포맷으로 데이터 전송:

`curl {{[-d|--data]}} {{'{"name":"bob"}'}} {{[-H|--header]}} {{'Content-Type: application/json'}} {{http://example.com/users/123}}`

- 리소스에 대한 클라이언트 인증서 및 키 전달, 인증서 유효성 검사 생략:

`curl {{[-E|--cert]}} {{클라이언트.pem}} --key {{키.pem}} {{[-k|--insecure]}} {{https://example.com}}`

- 호스트 이름을 사용자 지정 IP 주소로 해결하고, 상세한([v]erbose) 출력 결과를 표시 (사용자 지정 DNS resolution을 위해 `/etc/hosts` 파일을 편집하는 것과 유사):

`curl {{[-v|--verbose]}} --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
