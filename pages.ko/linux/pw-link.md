# pw-link

> PipeWire에서 포트 간의 링크를 관리.
> 더 많은 정보: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- 모든 오디오 출력 및 입력 포트와 해당 ID 나열:

`pw-link {{[-oiI|--output --input --id]}}`

- 출력 포트와 입력 포트 간 링크 생성:

`pw-link {{출력_포트_이름}} {{입력_포트_이름}}`

- 두 포트 간 연결 해제:

`pw-link {{[-d|--disconnect]}} {{출력_포트_이름}} {{입력_포트_이름}}`

- 모든 링크와 해당 ID 나열:

`pw-link {{[-lI|--links --id]}}`

- 도움말 표시:

`pw-link {{[-h|--help]}}`
