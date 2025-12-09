# foreman

> Procfile 기반 애플리케이션 관리 도구.
> 더 많은 정보: <https://manned.org/foreman>.

- 현재 디렉토리의 Procfile로 애플리케이션 시작:

`foreman start`

- 지정된 Procfile로 애플리케이션 시작:

`foreman start -f {{Procfile}}`

- 특정 애플리케이션 시작:

`foreman start {{프로세스}}`

- Procfile 형식 검증:

`foreman check`

- 프로세스 환경과 함께 일회성 명령 실행:

`foreman run {{명령}}`

- "worker"라는 이름의 프로세스를 제외한 모든 프로세스 시작:

`foreman start -m all=1,{{worker}}=0`
