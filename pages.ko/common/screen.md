# screen

> 원격 서버에서 세션을 열어 유지. 단일 SSH 연결로 여러 창을 관리.
> 같이 보기: `tmux`, `zellij`.
> 더 많은 정보: <https://manned.org/screen>.

- 새 screen 세션 시작:

`screen`

- 새 이름 지정 screen 세션 시작:

`screen -S {{세션_이름}}`

- 새로운 데몬을 시작하고 출력을 `screenlog.x`에 기록:

`screen -dmLS {{세션_이름}} {{명령}}`

- 열린 screen 세션 표시:

`screen -ls`

- 열린 screen에 다시 연결:

`screen -r {{세션_이름}}`

- screen 내부에서 분리:

`<Ctrl a><d>`

- 현재 screen 세션 종료:

`<Ctrl a><k>`

- 분리된 screen 종료:

`screen -X -S {{세션_이름}} quit`
