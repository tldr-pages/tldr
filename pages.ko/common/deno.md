# deno

> JavaScript, TypeScript, WebAssembly를 위한 보안 중심 런타임.
> `npm` 또는 `jsr`를 통한 의존성 관리와 bench, bundle, doc, coverage 등의 도구를 포함.
> 더 많은 정보: <https://docs.deno.com/runtime/reference/cli/>.

- REPL(대화형 쉘, Read-Eval-Print Loop)을 시작:

`deno`

- sample이라는 이름의 새로운 프로젝트 생성하고 테스트 실행:

`deno init sample && cd sample && deno test`

- 파일을 안전하게 실행. (필요시 네트워크, 파일 읽기 등 권한 요청):

`deno run {{경로/대상/파일.ts}}`

- 명시적인 권한을 지정하거나 모든 권한을 허용하여 실행 (신뢰할 수 있는 경우에만 사용):

`deno run {{[--allow-env|--allow-net|--allow-write|--allow-all]}} {{jsr:@deno/deployctl}}`

- `deno.json`의 작업 또는 `package.json`의 스크립트를 목록으로 표시하고 실행:

`deno task`

- `deno.json` 또는 `package.json`에 정의된 의존성을 설치 (lock 파일 포함):

`deno install`

- 타입 검사, 포맷, 린트를 수행 (가능한 경우 자동 수정):

`deno check && deno fmt && deno lint --fix`

- 스크립트, 의존성, 런타임을 포함한 단일 실행 파일을 생성:

`deno compile {{경로/대상/파일.ts}}`
