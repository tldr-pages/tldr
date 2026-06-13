# sqlmap

> SQL 인젝션 취약점을 탐지하고 악용.
> 더 많은 정보: <https://github.com/sqlmapproject/sqlmap/wiki/Usage>.

- 단일 대상 URL에 대해 sqlmap 실행:

`python sqlmap.py {{[-u|--url]}} "{{http://www.example.com/vuln.php?id=1}}"`

- POST 요청으로 데이터 전송 (`--data`는 POST 요청을 의미):

`python sqlmap.py {{[-u|--url]}} "{{http://www.example.com/vuln.php}}" --data="{{id=1}}"`

- 매개변수 구분자 변경 (기본값은 &):

`python sqlmap.py {{[-u|--url]}} "{{http://www.example.com/vuln.php}}" --data="{{query=foobar;id=1}}" --param-del="{{;}}"`

- `./txt/user-agents.txt`에서 무작위 `User-Agent` 선택 및 사용:

`python sqlmap.py {{[-u|--url]}} "{{http://www.example.com/vuln.php}}" --random-agent`

- HTTP 프로토콜 인증을 위한 사용자 자격 증명 제공:

`python sqlmap.py {{[-u|--url]}} "{{http://www.example.com/vuln.php}}" --auth-type {{Basic}} --auth-cred "{{testuser:testpass}}"`
