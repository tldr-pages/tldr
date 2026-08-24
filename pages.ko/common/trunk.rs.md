# trunk

> Rust WASM 웹 애플리케이션을 번들링하고 로컬에서 제공.
> 더 많은 정보: <https://trunkrs.dev/commands/>.

- 애플리케이션을 릴리스 모드로 빌드하고, 로컬에서 실행:

`trunk serve --release`

- 애플리케이션을 빌드하고 지정한 포트에서 실행:

`trunk serve {{[-p|--port]}} {{포트}}`

- 지정한 출력 디렉터리에 프로덕션 빌드를 생성:

`trunk build --release {{[-d|--dist]}} {{경로/대상/출력_디렉터리}}`

- 하위 디렉터리에서 호스팅하기 위해 특정 공개 URL 경로를 사용하여 빌드:

`trunk build --release --public-url /{{경로/대상/애플리케이션_하위디렉터리}}`

- 출력 디렉터리를 정리:

`trunk clean`
