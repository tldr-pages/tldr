# bun build

> Bun의 고속 네이티브 번들러를 사용해 JavaScript 및 Typescript 파일을 번들링.
> 더 많은 정보: <https://bun.com/docs/bundler>.

- 엔트리 포인트를 단일 파일로 묶어서 출력:

`bun build {{경로/대상/엔트리.ts}} --outfile {{경로/대상/출력파일.js}}`

- 여러 엔트리 포인트를 출력 디렉터리로 번들링:

`bun build {{경로/대상/엔트리1.ts 경로/대상/엔트리2.ts ...}} --outdir {{경로/대상/출력_디렉터리}}`

- 디버깅용 소스 맵을 포함하여 번들링:

`bun build {{경로/대상/엔트리.ts}} --outfile {{경로/대상/출력.js}} --sourcemap`

- 프로덕션용으로 최소화해 번들링:

`bun build {{경로/대상/엔트리.ts}} --outfile {{경로/대상/출력.js}} --minify`

- 지정한 타겟 환경에 맞게 번들링:

`bun build {{경로/대상/엔트리.ts}} --outfile {{경로/대상/출력.js}} --target {{browser|bun|node}}`

- 독립 실행 파일로 번들링:

`bun build {{경로/대상/엔트리.ts}} --compile --outfile {{경로/대상/실행파일}}`

- 파일 변경을 감지하여 자동으로 다시 빌드:

`bun build {{경로/대상/엔트리.ts}} --outfile {{경로/대상/출력.js}} --watch`

- 출력 파일에 포함되지 않는 외부 의존성과 함께 번들링:

`bun build {{경로/대상/엔트리.ts}} --outfile {{경로/대상/출력.js}} {{[-e|--external]}} {{react react-dom}}`
