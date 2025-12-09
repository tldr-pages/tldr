# zapier scaffold

> 통합에 시작 트리거, 생성, 검색 또는 리소스를 추가합니다.
> 더 많은 정보: <https://platform.zapier.com/reference/cli#scaffold>.

- 새 트리거, 생성, 검색 또는 리소스 스캐폴드:

`zapier scaffold {{trigger|search|create|resource}} {{명사}}`

- 스캐폴드된 파일의 사용자 지정 대상 폴더 지정:

`zapier scaffold {{trigger|search|create|resource}} {{명사}} {{[-d|--dest]}}={{경로/대상/폴더}}`

- 스캐폴딩 시 기존 파일 덮어쓰기:

`zapier scaffold {{trigger|search|create|resource}} {{명사}} {{[-f|--force]}}`

- 스캐폴드된 파일에서 주석 제외:

`zapier scaffold {{trigger|search|create|resource}} {{명사}} --no-help`

- 추가 디버깅 출력 표시:

`zapier scaffold {{[-d|--debug]}}`
