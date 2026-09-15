# qgis_process

> GUI를 실행하지 않고 명령줄에서 QGIS 처리 알고리즘을 실행.
> 관련 항목: `qgis`.
> 더 많은 정보: <https://docs.qgis.org/latest/en/docs/user_manual/processing/standalone.html>.

- 사용 가능한 모든 처리 알고리즘 목록 표시:

`qgis_process list`

- 지정한 알고리즘의 도움말 표시:

`qgis_process help {{알고리즘_아이디}}`

- 매개변수를 지정하여 처리 알고리즘 실행:

`qgis_process run {{알고리즘_아이디}} {{--PARAMETER1=value1 --PARAMETER2=value2 ...}}`

- 처리 알고리즘을 실행하고 결과를 JSON 형식으로 출력:

`qgis_process --json run {{알고리즘_아이디}} {{--PARAMETER1=값1 --PARAMETER2=값2 ...}}`

- 더 빠른 시작을 위해 플러그인을 로드하지 않고 처리 알고리즘 실행:

`qgis_process --skip-loading-plugins run {{알고리즘_아이디}} {{--PARAMETER1=값1 --PARAMETER2=값2 ...}}`

- 디스플레이가 없는 헤드리스 서버에서 처리 알고리즘 실행:

`QT_QPA_PLATFORM=offscreen qgis_process run {{알고리즘_아이디}} {{--PARAMETER1=값1 --PARAMETER2=값2 ...}}`

- 사용 가능한 플러그인 및 활성화된 플러그인 목록 표시:

`qgis_process plugins`

- 설치된 플러그인 활성화 또는 비활성화:

`qgis_process plugins {{enable|disable}} {{플러그인_이름}}`
