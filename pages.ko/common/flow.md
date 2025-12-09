# flow

> JavaScript용 정적 유형 검사기.
> 더 많은 정보: <https://flow.org/en/docs/cli/>.

- 흐름 검사를 실행:

`flow`

- 흐름별로 검사 중인 파일을 확인:

`flow ls`

- 디렉토리의 모든 파일에 대해 유형 검사를 실행:

`flow batch-coverage --show-all --strip-root {{경로/대상/디렉터리}}`

- 라인별 유형 적용 범위 통계 표시:

`flow coverage --color {{경로/대상/파일.jsx}}`
