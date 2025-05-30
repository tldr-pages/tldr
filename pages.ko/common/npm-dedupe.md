# npm dedupe

> `node_modules` 디렉토리에서 중복을 줄입니다.
> 더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-dedupe>.

- `node_modules`의 패키지 중복 제거:

`npm dedupe`

- 중복 제거 시 `package-lock.json` 또는 `npm-shrinkwrap.json`을 따르기:

`npm dedupe --lock`

- 엄격 모드로 중복 제거 실행:

`npm dedupe --strict`

- 중복 제거 시 선택적/피어 의존성 건너뛰기:

`npm dedupe --omit {{optional|peer}}`

- 문제 해결을 위한 자세한 로깅 활성화:

`npm dedupe --loglevel verbose`

- 특정 패키지에 대해 중복 제거 제한:

`npm dedupe {{패키지_이름}}`
