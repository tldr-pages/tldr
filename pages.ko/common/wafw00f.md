# wafw00f

> 웹 애플리케이션 방화벽(WAF) 제품을 식별하고 지문을 채취하여 사이트를 보호.
> 더 많은 정보: <https://github.com/EnableSecurity/wafw00f/wiki/Usage#arguments-list>.

- 웹사이트가 WAF를 사용 중인지 확인:

`wafw00f {{https://www.example.com}}`

- 첫 번째 일치 항목에서 멈추지 않고 감지 가능한 모든 WAF 테스트:

`wafw00f --findall {{https://www.example.com}}`

- 요청을 프록시(예: BurpSuite)를 통해 전달:

`wafw00f --proxy {{http://localhost:8080}} {{https://www.example.com}}`

- 특정 WAF 제품 테스트 (`wafw00f -l`을 실행하여 지원되는 모든 WAF 목록 확인):

`wafw00f --test {{Cloudflare|Cloudfront|Fastly|ZScaler|...}} {{https://www.example.com}}`

- 파일에서 사용자 지정 헤더 전달:

`wafw00f --headers {{경로/대상/헤더.txt}} {{https://www.example.com}}`

- 파일에서 대상 입력을 읽고 자세한 출력 표시 (더 많은 자세한 출력을 위해 `v`를 여러 번 사용):

`wafw00f --input {{경로/대상/urls.txt}} -v{{v}}`

- 감지 가능한 모든 WAF 나열:

`wafw00f --list`
