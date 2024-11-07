# pnpm outdated

> 오래된 패키지 확인.
> 인수를 제공하여 설치된 패키지의 일부 집합으로 확인을 제한할 수 있습니다 (패턴 지원).
> 더 많은 정보: <https://pnpm.io/cli/outdated>.

- 오래된 패키지 확인:

`pnpm outdated`

- 모든 워크스페이스 패키지에서 발견된 오래된 의존성 확인:

`pnpm outdated -r`

- 패키지 선택기를 사용하여 오래된 패키지 필터링:

`pnpm outdated --filter {{패키지_선택기}}`

- 오래된 패키지를 [g]lobal로 나열:

`pnpm outdated --global`

- 오래된 패키지의 세부정보 출력:

`pnpm outdated --long`

- 특정 형식으로 오래된 의존성 출력:

`pnpm outdated --format {{형식}}`

- `package.json`의 사양을 충족하는 버전만 출력:

`pnpm outdated --compatible`

- 오래된 [D]ev 의존성만 확인:

`pnpm outdated --dev`
