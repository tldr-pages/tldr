# neato

> `graphviz` 파일에서 `선형 무방향` 네트워크 그래프의 이미지를 렌더링.
> 레이아웃: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage`, `patchwork`.
> 더 많은 정보: <https://graphviz.org/doc/info/command.html>.

- 입력 파일 이름과 출력 형식에 기반하여 PNG 이미지 렌더링 (대문자 -O 사용):

`neato -T {{png}} -O {{경로/대상/입력.gv}}`

- 지정된 출력 파일 이름으로 SVG 이미지 렌더링 (소문자 -o 사용):

`neato -T {{svg}} -o {{경로/대상/이미지.svg}} {{경로/대상/입력.gv}}`

- PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON, 또는 DOT 형식으로 출력 렌더링:

`neato -T {{형식}} -O {{경로/대상/입력.gv}}`

- `stdin`과 `stdout`을 사용하여 GIF 이미지 렌더링:

`echo "{{graph {this -- that} }}" | neato -T {{gif}} > {{경로/대상/이미지.gif}}`

- 도움말 표시:

`neato -?`
