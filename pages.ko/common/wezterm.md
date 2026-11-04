# wezterm

> Wez's Terminal Emulator - 강력한 크로스 플랫폼 터미널 에뮬레이터 및 멀티플렉서.
> `cli` 등의 일부 하위 명령은 각각 별도의 사용 문서를 제공.
> 더 많은 정보: <https://wezterm.org/cli/general>.

- 새로운 Wezterm 프로세스를 시작하고 창을 생성:

`wezterm`

- 새로운 Wezterm 창에서 `ssh` 세션을 연결:

`wezterm ssh {{사용자}}@{{호스트}}:{{포트}}`

- 멀티플렉서 (`wezterm-mux-server`)에 연결:

`wezterm connect {{도메인_이름}}`

- 터미널에 이미지를 출력:

`wezterm imgcat {{경로/대상/이미지}}`

- 터미널 세션을 asciicast로 녹화 (기본적으로 `/tmp`에 저장):

`wezterm record`

- 녹화된 asciicast 터미널 세션 재생:

`wezterm replay {{경로/대상/cast_파일}}`

- 사용할 설정 파일 지정 (기본 설정 파일 탐색 방법을 무시):

`wezterm --config-file {{경로/대상/구성_파일}}`

- 도움말 표시:

`wezterm help`
