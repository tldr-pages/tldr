# opencode stats

> 토큰 사용량 및 비용 통계를 표시하는 명령어.
> 더 많은 정보: <https://opencode.ai/docs/cli#stats>.

- 통계 출력:

`opencode stats`

- 최근 N일간 통계 출력:

`opencode stats --days {{30}}`

- 모델별 사용량 포함 통계 출력:

`opencode stats --models`

- 사용량 기준 상위 N개 모델 출력:

`opencode stats --models {{5}}`

- 특정 프로젝트의 통계 출력 (생략 시 현재 프로젝트 사용):

`opencode stats --project {{프로젝트_이름}}`

- 상위 N개 도구 출력:

`opencode stats --tools {{10}}`

- 도움말 출력:

`opencode stats {{[-h|--help]}}`
