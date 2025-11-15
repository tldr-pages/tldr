# tsc

> TypeScript 컴파일러.
> 더 많은 정보: <https://www.typescriptlang.org/docs/handbook/compiler-options.html>.

- `foobar.ts` TypeScript 파일을 `foobar.js` JavaScript 파일로 컴파일:

`tsc {{foobar.ts}}`

- 특정 목표 구문을 사용하여 TypeScript 파일을 JavaScript로 컴파일 (기본값은 `ES3`):

`tsc --target {{ES5|ES2015|ES2016|ES2017|ES2018|ESNEXT}} {{foobar.ts}}`

- 사용자 정의 이름으로 TypeScript 파일을 JavaScript 파일로 컴파일:

`tsc --outFile {{출력.js}} {{입력.ts}}`

- `tsconfig.json` 파일에 정의된 TypeScript 프로젝트의 모든 `.ts` 파일 컴파일:

`tsc --build {{tsconfig.json}}`

- 명령줄 옵션 및 인수를 텍스트 파일에서 가져와 컴파일러 실행:

`tsc @{{인수.txt}}`

- 여러 JavaScript 파일을 타입 체크하고, 오류만 출력:

`tsc --allowJs --checkJs --noEmit {{src/**/*.js}}`

- 코드가 변경될 때 자동으로 다시 컴파일하는 감시 모드에서 컴파일러 실행:

`tsc --watch`
