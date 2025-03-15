# pw-dot

> PipeWire 그래프의 `.dot` 파일 생성.
> 같이 보기: `dot`, 그래프 렌더링을 위해.
> 더 많은 정보: <https://docs.pipewire.org/page_man_pw-dot_1.html>.

- `pw.dot` 파일로 그래프 생성:

`pw-dot`

- `pw-dump` JSON 파일에서 객체 읽기:

`pw-dot {{[-j|--json]}} {{경로/대상/파일.json}}`

- [o]utput 파일 지정, 모든 객체 유형 표시:

`pw-dot {{[-o|--output]}} {{경로/대상/파일.dot}} {{[-a|--all]}}`

- 모든 객체 속성을 표시하며 `.dot` 그래프를 `stdout`에 출력:

`pw-dot {{[-o|--output]}} - {{[-d|--detail]}}`

- [r]emote 인스턴스에서 그래프를 생성, 연결된 객체만 표시:

`pw-dot {{[-r|--remote]}} {{원격_이름}} {{[-s|--smart]}}`

- 기본적으로 dot의 위에서 아래로가 아닌 왼쪽에서 오른쪽으로 그래프 정렬:

`pw-dot {{-L|--lr}}`

- 엣지를 90도 각도로 사용하여 그래프 정렬:

`pw-dot {{-9|--90}}`

- 도움말 표시:

`pw-dot {{[-h|--help]}}`
