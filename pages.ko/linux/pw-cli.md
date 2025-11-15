# pw-cli

> PipeWire 인스턴스의 모듈, 객체, 노드, 장치, 링크 등을 관리.
> 더 많은 정보: <https://docs.pipewire.org/page_man_pw-cli_1.html>.

- 모든 노드(싱크 및 소스)와 그 ID를 출력:

`pw-cli list-objects Node`

- 특정 ID를 가진 객체에 대한 정보 출력:

`pw-cli info {{4}}`

- 모든 객체의 정보 출력:

`pw-cli info all`
