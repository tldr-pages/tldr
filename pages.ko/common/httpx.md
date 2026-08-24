# httpx

> 여러 프로브를 한 번에 실행하기 위해 Go로 작성된 빠르고 다목적 HTTP 도구 키트.
> 참고: 동일한 명령 이름을 가진 관련 없는 Python's HTTPX와 혼동하지 말것.
> 더 많은 정보: <https://docs.projectdiscovery.io/opensource/httpx/running>.

- 프로브 상태를 표시하는 [u]RL, 호스트, IP 주소 또는 서브넷 (CIDR 표기법)에 대해 프로브를 실행:

`httpx -probe {{[-u|-target]}} {{url|host|ipaddress|subnet_with_cidr}}`

- `subfinder`의 입력으로 상태 코드([s]tatus [c]ode)를 표시하는 여러 호스트에 대해 프로브를 실행:

`subfinder {{[-d|-domain]}} {{example.com}} | httpx {{[-sc|-status-code]}}`

- 감지된([d]etected) 기술([t]echnology) 및 응답시간([r]esponse [t]ime)을 보여주는 파일에서 호스트 목록([l]ist)에 대해 제한된 속도로 실행:

`httpx {{[-rl|-rate-limit]}} {{150}} {{[-l|-list]}} {{경로/대상/개행으로_구분된_호스트_목록}} {{[-td|-tech-detect]}} {{[-rt|-response-time]}}`

- 웹페이지 제목, 사용 중인 CDN/WAF 및 페이지 콘텐츠 해시를 표시하는 [u]RL에 대해 프로브를 실행:

`httpx {{[-u|-target]}} {{주소}} -title -cdn -hash {{sha256}}`

- 사용자 정의된 포트([p]orts)와 특정 초 후 시간 초과가 있는 호스트 목록에 대해 프로블를 실행:

`httpx -probe {{[-u|-target]}} {{호스트1,호스트2,...}} {{[-p|-ports]}} http:{{80,8000-8080}},https:{{443,8443}} -timeout {{10}}`

- 특정 응답 코드([c]odes)를 필터링하여([f]iltering), 호스트 목록에 대해 프로브를 실행:

`httpx {{[-u|-target]}} {{호스트1,호스트2,...}} {{[-fc|-filter-code]}} {{400,401,404}}`

- 특정 응답 코드([c]odes)와 일치하는([m]atching) 호스트 목록에 대해 프로브를 실행:

`httpx {{[-u|-target]}} {{호스트1,호스트2,...}} {{[-mc|-match-code]}} {{200,301,304}}`

- 특정 경로의 스크린샷([s]creenshots)을 저장하고([s]aving) 스크린샷 타임아웃([s]creenshot [t]imeouts)을 사용하여 URL에 대해 프로브를 실행 (리소스는 `./output`에 저장됨):

`httpx {{[-u|-target]}} {{https://www.github.com}} -path {{/tldr-pages/tldr,/projectdiscovery/httpx}} {{[-ss|-screenshot]}} {{[-st|-screenshot-timeout]}} {{10}}`
