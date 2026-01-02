# katana

> 자동화 파이프라인에서의 실행에 중점을 둔 빠른 크롤러로, 헤드리스 및 비헤드리스 크롤링을 모두 제공합니다.
> 같이 보기: `gau`, `scrapy`, `waymore`.
> 더 많은 정보: <https://docs.projectdiscovery.io/opensource/katana/usage>.

- URL 목록을 크롤링:

`katana -list {{https://example.com,https://google.com,...}}`

- Chromium을 사용하여 헤드리스 모드로 URL 크롤링:

`katana -u {{https://example.com}} -headless`

- `subfinder`를 사용하여 서브도메인을 찾고, [p]a[s]sive 소스(Wayback Machine, Common Crawl, AlienVault)로 URL 검색:

`subfinder -list {{경로/대상/domains.txt}} | katana -passive`

- 프록시(http/socks5)를 통해 요청 전달하고 파일에서 사용자 정의 [H]eaders 사용:

`katana -proxy {{http://127.0.0.1:8080}} -headers {{경로/대상/headers.txt}} -u {{https://example.com}}`

- 크롤링 [s]trategy, 크롤링할 하위 디렉토리의 [d]epth, 속도 제한(초당 요청 수) 지정:

`katana -strategy {{depth-first|breadth-first}} -depth {{값}} -rate-limit {{값}} -u {{https://example.com}}`

- `subfinder`를 사용하여 서브도메인을 찾고, 각 서브도메인을 최대 시간 동안 크롤링하며 결과를 [o]utput 파일에 저장:

`subfinder -list {{경로/대상/domains.txt}} | katana -crawl-duration {{값}} -output {{경로/대상/output.txt}}`
