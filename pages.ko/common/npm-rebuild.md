# npm rebuild

> Node 또는 의존성 변경 후 네이티브 Node.js 패키지를 다시 빌드하는 명령어.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-rebuild/>.

- 특정 패키지 재빌드:

`npm {{[rb|rebuild]}} {{패키지}}`

- 모든 설치된 패키지 재빌드:

`npm {{[rb|rebuild]}}`

- 상세 출력과 함께 재빌드:

`npm {{[rb|rebuild]}} --verbose`

- 특정 디렉터리에서 패키지 재빌드:

`npm {{[rb|rebuild]}} --prefix {{경로/대상/디렉터리}} {{패키지}}`

- npm 캐시를 사용하지 않고 재빌드:

`npm {{[rb|rebuild]}} --no-cache`

- 전역 모드에서 재빌드:

`npm {{[rb|rebuild]}} {{[-g|--global]}}`
