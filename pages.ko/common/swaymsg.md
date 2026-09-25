# swaymsg

> 실행 중인 Sway 인스턴스에 IPC를 통해 메시지를 전송.
> 사용 가능한 명령은 <https://github.com/swaywm/sway/blob/master/sway/sway.5.scd> 문서를 참고.
> 더 많은 정보: <https://github.com/swaywm/sway/blob/master/swaymsg/swaymsg.1.scd>.

- Sway 명령어 실행:

`swaymsg {{명령어}}`

- workspace 목록 표시:

`swaymsg {{[-t|--type]}} get_workspaces`

- 입력 장치 목록 표시:

`swaymsg {{[-t|--type]}} get_inputs`

- 출력 장치 목록 표시:

`swaymsg {{[-t|--type]}} get_outputs`

- 열려 있는 모든 창, 컨테이너, 출력 장치 및 작업 공간의 레이아웃 트리 표시:

`swaymsg {{[-t|--type]}} get_tree`
