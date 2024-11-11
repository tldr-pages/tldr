# pnpx

> npm 패키지의 바이너리를 `npm` 대신 `pnpm`을 사용하여 직접 실행.
> 참고: 이 명령은 사용이 중단되었습니다! 대신 `pnpm exec` 및 `pnpm dlx`를 사용하세요.
> 더 많은 정보: <https://cuyl.github.io/pnpm.github.io/pnpx-cli>.

- 주어진 `npm` 모듈에서 바이너리 실행:

`pnpx {{모듈_이름}}`

- 주어진 `npm` 모듈이 여러 바이너리를 포함하는 경우 특정 바이너리 실행:

`pnpx --package {{패키지_이름}} {{모듈_이름}}`

- 도움말 표시:

`pnpx --help`
