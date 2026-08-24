# composer audit

> PHP 프로젝트의 의존성을 분석하여 알려진 보안 취약점을 탐지하고 영향을 받는 패키지를 표시.
> 관련 항목: `composer`.
> 더 많은 정보: <https://getcomposer.org/doc/03-cli.md#audit>.

- 현재 프로젝트의 보안 취약점을 확인:

`composer audit`

- 감사(audit)에서 개발 의존성을 제외:

`composer audit --no-dev`

- 출력 형식으로 취약점을 필터링:

`composer audit --format {{table|plain|json|summary}}`

- 감사 결과를 JSON 형식으로 파일에 저장:

`composer audit --format json > audit_report.json`

- 프로젝트의 특정 패키지가 보안 문제의 영향을 받는지 확인:

`composer audit {{벤더}}/{{패키지}}`
