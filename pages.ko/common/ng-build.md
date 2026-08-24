# ng build

> Angular 애플리케이션 또는 라이브러리를 `dist/` 출력 디렉터리로 컴파일.
> 더 많은 정보: <https://angular.dev/cli/build>.

- Angular 애플리케이션 또는 라이브러리 빌드:

`ng {{[b|build]}}`

- 워크스페이스 루트 기준으로 출력 경로 지정:

`ng {{[b|build]}} --output-path {{경로/대상/디렉터리}}`

- Ahead-of-Time (AOT) 컴파일 활성화:

`ng {{[b|build]}} --aot`

- 콘솔에 빌드 진행 상황 표시:

`ng {{[b|build]}} --progress`

- 빌드 시 상세 로그 출력:

`ng {{[b|build]}} --verbose`

- 재빌드 시, 터미널 화면 자동으로 정리:

`ng {{[b|build]}} --clear-screen`

- 소스 파일 변경 시 자동 재빌드:

`ng {{[b|build]}} --watch`
