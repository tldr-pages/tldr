# circo

> `graphviz` 파일에서 `circular` 네트워크 그래프의 이미지를 렌더링.
> 레이아웃: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` & `patchwork`.
> 더 많은 정보: <https://graphviz.org/doc/info/command.html>.

- 입력 파일 이름 및 출력 형식(대문자 -O)을 기반으로 하는 파일 이름으로 PNG 이미지를 렌더링:

`circo -T {{png}} -O {{경로/대상/입력.gv}}`

- 지정된 출력 파일명으로 SVG(소문자 -o) 이미지를 렌더링:

`circo -T {{svg}} -o {{경로/대상/이미지.svg}} {{경로/대상/입력.gv}}`

- 출력을 PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON, 또는 DOT 형식으로 렌더링:

`circo -T {{포맷}} -O {{경로/대상/입력.gv}}`

- `stdin` 및 `stdout`을 사용하여 GIF 이미지 렌더링:

`echo "{{digraph {this -> that} }}" | circo -T {{gif}} > {{경로/대상/이미지.gif}}`

- 도움말 표시:

`circo -?`
