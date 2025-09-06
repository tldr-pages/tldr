# gitui

> Git용 경량 키보드 전용 TUI.
> 참고: `tig`, `git-gui`.
> 더 많은 정보: <https://github.com/extrawurst/gitui>.

- 색상 테마를 지정 (기본값은 `theme.ron`):

`gitui --theme {{테마}}`

- 로깅 출력을 캐시 디렉터리에 저장:

`gitui --logging`

- tick 기반 업데이트 대신, 알림 기반 파일 시스템 감시자를 사용:

`gitui --watcher`

- 버그 리포트를 생성:

`gitui --bugreport`

- 특정 Git 레포지토리 사용:

`gitui --directory {{경로/대상/디렉터리}}`

- 특정 작업 디렉터리 사용:

`gitui --workdir {{경로/대상/디렉터리}}`

- 도움말 표시:

`gitui --help`

- 버전 정보 표시:

`gitui --version`
