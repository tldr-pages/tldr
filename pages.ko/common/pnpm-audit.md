# pnpm audit

> 프로젝트 의존성을 스캔합니다.
> 설치된 패키지에서 알려진 보안 문제를 확인합니다.
> 더 많은 정보: <https://pnpm.io/cli/audit>.

- 프로젝트의 취약점 식별:

`pnpm audit`

- 취약점 자동 수정:

`pnpm audit fix`

- JSON 형식의 보안 보고서 생성:

`pnpm audit --json > {{경로/대상/audit-report.json}}`

- [D]ev 의존성만 감사:

`pnpm audit --dev`

- [P]roduction 의존성만 감사:

`pnpm audit --prod`

- 선택적 의존성을 감사에서 제외:

`pnpm audit --no-optional`

- 감사 과정에서 레지스트리 오류 무시:

`pnpm audit --ignore-registry-errors`

- 심각도별로 자문 필터링 (low, moderate, high, critical):

`pnpm audit --audit-level {{심각도}}`
