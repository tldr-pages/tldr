# zizmor

> GitHub Actions 워크플로우와 액션 정의에서 보안 취약점 탐지 도구.
> 더 많은 정보: <https://docs.zizmor.sh/quickstart/>.

- 현재 디렉터리의 모든 워크플로우 및 액션 검사:

`zizmor .`

- 특정 워크플로우 파일 검사:

`zizmor {{경로/대상/워크플로우.yml}}`

- 원격 GitHub 저장소 검사 (GitHub 토큰 필요):

`zizmor --gh-token {{토큰}} {{사용자명/저장소}}`

- 오프라인 검사만 수행 (네트워크 요청 없음):

`zizmor {{[-o|--offline]}} {{경로/대상/워크플로우.yml}}`

- SARIF 형식으로 결과 출력:

`zizmor --format sarif {{경로/대상/워크플로우.yml}}`

- 최소 심각도 기준으로 결과 필터링:

`zizmor --min-severity {{informational|low|medium|high}} .`

- 도움말 표시:

`zizmor {{[-h|--help]}}`

- 버전 정보 표시:

`zizmor {{[-v|--version]}}`
