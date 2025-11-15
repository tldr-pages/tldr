# qtile

> Python으로 작성 및 구성된 완전한 기능의 해킹 가능한 타일링 윈도우 매니저.
> 더 많은 정보: <https://docs.qtile.org/en/latest/manual/commands/shell/index.html>.

- 윈도우 매니저를 시작 (이미 실행 중이 아니라면, `.xsession` 또는 유사한 곳에서 실행하는 것이 이상적):

`qtile start`

- 설정 파일에 컴파일 오류가 있는지 확인 (기본 위치는 `~/.config/qtile/config.py`):

`qtile check`

- 현재 리소스 사용 정보 표시:

`qtile top --force`

- `test-group`이라는 그룹에서 `xterm` 프로그램을 플로팅 윈도우로 열기:

`qtile run-cmd --group {{test-group}} --float {{xterm}}`

- 윈도우 매니저 다시 시작:

`qtile cmd-obj --object cmd --function restart`
