# golangci-lint

> 병렬 처리, 스마트하고 빠른 Go 린터 실행 도구로 주요 IDE와 통합되며 YAML 구성을 지원합니다.
> 더 많은 정보: <https://golangci-lint.run/welcome/quick-start/>.

- 현재 폴더에서 린터 실행:

`golangci-lint run`

- 활성화 및 비활성화된 린터 목록 표시 (참고: 비활성화된 린터는 마지막에 표시되며, 활성화된 린터로 착각하지 마세요):

`golangci-lint linters`

- 특정 린터를 이 실행에서 [E]nable:

`golangci-lint run --enable {{린터}}`
