# ts-node

> TypeScript 코드를 컴파일 없이 직접 실행.
> 더 많은 정보: <https://typestrong.org/ts-node/docs/options>.

- TypeScript 파일을 컴파일 없이 실행 (`node` + `tsc`):

`ts-node {{경로/대상/파일.ts}}`

- `tsconfig.json`을 로드하지 않고 TypeScript 파일 실행:

`ts-node --skip-project {{경로/대상/파일.ts}}`

- 리터럴로 전달된 TypeScript 코드 평가:

`ts-node --eval '{{console.log("Hello World")}}'`

- 스크립트 모드로 TypeScript 파일 실행:

`ts-node --script-mode {{경로/대상/파일.ts}}`

- TypeScript 파일을 실행하지 않고 JavaScript로 트랜스파일:

`ts-node --transpile-only {{경로/대상/파일.ts}}`

- TS-Node 도움말 표시:

`ts-node --help`
