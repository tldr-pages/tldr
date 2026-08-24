# i3-msg

> IPC를 사용해 실행중인 i3 인스턴스에 메시지를 전송.
> 사용 가능한 명령어는 <https://i3wm.org/docs/userguide.html#list_of_commands>를 참고.
> 더 많은 정보: <https://manned.org/i3-msg>.

- i3 명령어 실행:

`i3-msg {{명령어}}`

- 워크스페이스 목록을 JSON 형식으로 출력:

`i3-msg -t get_workspaces`

- 열려있는 모든 창, 컨테이너, 출력, 워크스페이스의 레이아웃 트리를 JSON 형식으로 출력:

`i3-msg -t get_tree`
