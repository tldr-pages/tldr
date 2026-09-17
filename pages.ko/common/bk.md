# bk

> Buildkite 빌드, 파이프라인 및 에이전트 관리.
> 더 많은 정보: <https://github.com/buildkite/cli#usage>.

- API 토큰 및 조직 설정:

`bk configure`

- 사용할 조직 선택:

`bk use {{조직_slug}}`

- `pipeline.yaml` 파일 초기화:

`bk init`

- 현재 조직의 모든 파이프라인 목록 표시:

`bk pipeline list`

- 파이프라인 빌드 실행:

`bk build create {{파이프라인_slug}}`

- 특정 빌드의 상태 확인:

`bk build view {{빌드_번호}}`

- 현재 조직의 모든 에이전트 목록 표시:

`bk agent list`

- 도움말 표시:

`bk {{[-h|--help]}}`
