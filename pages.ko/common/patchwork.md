# patchwork

> `그래프비즈` 파일에서 `squareified treemap` 네트워크 그래프의 이미지를 렌더링합니다.
> 레이아웃: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` 및 `patchwork`.
> 더 많은 정보: <https://graphviz.org/doc/info/command.html>.

- 입력 파일 이름과 출력 형식(대문자 -O)을 기반으로 PNG 이미지를 렌더링:

`patchwork -T {{png}} -O {{경로/대상/입력.gv}}`

- 지정된 출력 파일 이름(소문자 -o)으로 SVG 이미지를 렌더링:

`patchwork -T {{svg}} -o {{경로/대상/이미지.svg}} {{경로/대상/입력.gv}}`

- 출력을 PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON 또는 DOT 형식으로 렌더링:

`patchwork -T {{형식}} -O {{경로/대상/입력.gv}}`

- `stdin` 및 `stdout`을 사용하여 `gif` 이미지 렌더링:

`echo "{{digraph {this -> that} }}" | patchwork -T {{gif}} > {{경로/대상/이미지.gif}}`

- 도움말 표시:

`patchwork -?`
