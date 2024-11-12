# goku

> Karabiner 설정 관리.
> 더 많은 정보: <https://github.com/yqrashawn/GokuRakuJoudo>.

- 기본 설정을 사용하여 `karabiner.json` 생성:

`goku`

- 특정 `config.edn` 파일을 사용하여 `karabiner.json` 생성:

`goku --config {{경로/대상/config.edn}}`

- `karabiner.json`을 업데이트하는 대신 새로운 설정을 `stdout`으로 테스트 실행:

`goku --dry-run`

- `karabiner.json`을 업데이트하는 대신 전체 설정을 `stdout`으로 테스트 실행:

`goku --dry-run-all`

- 도움말 표시:

`goku --help`

- 버전 표시:

`goku --version`
