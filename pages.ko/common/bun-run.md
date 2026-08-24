# bun run

> JavaScript/TypeScript 파일을 실행하거나, `package.json`에 정의된 스크립트를 실행.
> 더 많은 정보: <https://bun.com/docs/runtime>.

- `package.json`에 정의된 스크립트 실행:

`bun run {{스크립트_이름}}`

- JavaScript 또는 TypeScript 파일 직접 실행:

`bun run {{경로/대상/파일.ts}}`

- 파일 변경 시 자동 재시작되는 "watch" 모드로 실행:

`bun run --watch {{경로/대상/파일.ts}}`

- 특정 설정 파일을 사용하여 실행:

`bun run {{[-c|--config]}} {{경로/대상/bunfig.toml}} {{경로/대상/파일.ts}}`
