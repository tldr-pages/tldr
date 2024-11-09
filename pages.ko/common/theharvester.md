# theHarvester

> 침투 테스트의 초기 단계에서 사용하도록 설계된 도구.
> 더 많은 정보: <https://github.com/laramies/theHarvester>.

- Google을 사용하여 도메인에 대한 정보 수집:

`theHarvester --domain {{도메인_이름}} --source google`

- 여러 소스를 사용하여 도메인에 대한 정보 수집:

`theHarvester --domain {{도메인_이름}} --source {{duckduckgo,bing,crtsh}}`

- 결과 제한 변경:

`theHarvester --domain {{도메인_이름}} --source {{google}} --limit {{200}}`

- XML 및 HTML 형식으로 출력 파일 두 개로 저장:

`theHarvester --domain {{도메인_이름}} --source {{google}} --file {{출력_파일_이름}}`

- 도움말 표시:

`theHarvester --help`
