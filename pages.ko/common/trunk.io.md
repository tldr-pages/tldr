# trunk

> 코드에 대해 린터(linters), 포맷터(formatters) 및 보안 분석 도구를 실행.
> 더 많은 정보: <https://docs.trunk.io/code-quality/overview/getting-started/commands-reference>.

- 저장소에서 trunk를 초기화:

`trunk init`

- 변경된 파일에 대해 적용 가능한 모든 린터와 포맷터를 실행:

`trunk check`

- 특정 파일에 대해 린터와 포맷터를 실행:

`trunk check {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 파일을 제자리에서 포맷:

`trunk fmt`

- 사용 가능한 모든 도구와 상태를 표시:

`trunk tools list`

- 특정 버전의 도구를 활성화:

`trunk tools enable {{도구}}@{{버전}}`

- 액션의 실행 기록을 출력:

`trunk actions history {{액션}}`
