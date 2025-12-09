# pidof

> 프로세스 이름을 사용하여 프로세스 ID를 가져옵니다.
> 더 많은 정보: <https://manned.org/pidof>.

- 주어진 이름의 모든 프로세스 ID 나열:

`pidof {{bash}}`

- 주어진 이름의 단일 프로세스 ID 나열:

`pidof -s {{bash}}`

- 주어진 이름의 스크립트를 포함한 프로세스 ID 나열:

`pidof -x {{스크립트.py}}`

- 주어진 이름의 모든 프로세스를 종료:

`kill $(pidof {{이름}})`
