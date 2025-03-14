# ip route show

> IP 라우팅 테이블 관리용 하위 명령어.
> 더 많은 정보: <https://manned.org/ip-route>.

- 라우팅 테이블 표시:

`ip {{[r|route]}} {{[s|show]}}`

- 메인 라우팅 테이블 표시 (첫 번째 예시와 동일):

`ip {{[r|route]}} {{[s|show]}} {{main|254}}`

- 로컬 라우팅 테이블 표시:

`ip {{[r|route]}} {{[s|show]}} {{[t|table]}} {{local|255}}`

- 모든 라우팅 테이블 표시:

`ip {{[r|route]}} {{[s|show]}} {{[t|table]}} {{all|unspec|0}}`

- 특정 장치에서만 경로 나열:

`ip {{[r|route]}} {{[s|show]}} dev {{eth0}}`

- 특정 범위 내의 경로 나열:

`ip {{[r|route]}} {{[s|show]}} {{[s|scope]}} link`

- 라우팅 캐시 표시:

`ip {{[r|route]}} {{[s|show]}} {{[c|cache]}}`

- IPv6 또는 IPv4 경로만 표시:

`ip {{-6|-4}} {{[r|route]}} {{[s|show]}}`
