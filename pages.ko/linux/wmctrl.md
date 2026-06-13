# wmctrl

> X 윈도우 매니저용 CLI.
> 더 많은 정보: <https://manned.org/wmctrl>.

- 윈도우 매니저가 관리하는 모든 창 나열:

`wmctrl -l`

- (부분적으로) 제목이 일치하는 첫 번째 창으로 전환:

`wmctrl -a {{창_제목}}`

- 창을 현재 작업공간으로 이동하고, 올려서 포커스를 줌:

`wmctrl -R {{창_제목}}`

- 작업공간으로 전환:

`wmctrl -s {{작업공간_번호}}`

- 창을 선택하고 전체 화면 전환:

`wmctrl -r {{창_제목}} -b toggle,fullscreen`

- 창을 선택하고 작업공간으로 이동:

`wmctrl -r {{창_제목}} -t {{작업공간_번호}}`
