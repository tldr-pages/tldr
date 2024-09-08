# browser-sync

> 파일 변경에 따라 브라우저를 업데이트 하는 로컬 웹 서버 시작.
> 더 많은 정보: <https://browsersync.io/docs/command-line>.

- 특정 디렉토리로부터 서버 시작:

`browser-sync start --server {{디렉토리/의/경로}} --files {{디렉토리/의/경로}}`

- 로컬 디렉토리에서 서버 시작, 일부 디렉토리에서 모든 CSS파일 확인:

`browser-sync start --server --files '{{디렉토리/의/경로/*.css}}'`

- 구성 파일 생성:

`browser-sync init`

- 구성 파일에서 브라우저 동기화 시작:

`browser-sync start --config {{config_파일}}`
