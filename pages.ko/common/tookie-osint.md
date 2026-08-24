# tookie-osint

> 사용자 이름 기반 공개 정보를 수집하는 OSINT 스캐너 .
> 더 많은 정보: <https://github.com/Alfredredbird/tookie-osint>.

- 사용자 이름 검색:

`tookie-osint {{[-u|--user]}} {{사용자명}}`

- JSON 형식으로 출력하고 10개의 스레드를 사용하여 사용자 이름 검색:

`tookie-osint {{[-u|--user]}} {{사용자명}} {{[-o|--output]}} json {{[-t|--threads]}} 10`

- 파일에 있는 여러 사용자 이름을 검색하고 CSV 형식으로 출력:

`tookie-osint {{[-U|--userfile]}} {{path/to/users.txt}} {{[-o|--output]}} csv`

- 프록시를 사용하여 사용자 이름을 검색하고 모든 결과 표시:

`tookie-osint {{[-u|--user]}} {{사용자명}} {{[-p|--proxy]}} {{http://127.0.0.1:8080}} {{[-a|--all]}}`

- 웹 스크래퍼를 활성화하여 사용자 이름 검색:

`tookie-osint {{[-u|--user]}} {{사용자명}} {{[-W|--webscraper]}}`

- 도움말 표시:

`tookie-osint {{[-h|--help]}}`
