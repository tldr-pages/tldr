# osage

> `graphviz` 파일에서 `clustered` 네트워크 그래프 이미지를 렌더링.
> 레이아웃: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` 및 `patchwork`.
> 더 많은 정보: <https://graphviz.org/doc/info/command.html>.

- 입력 파일 이름과 출력 형식에 기반하여 파일 이름이 정해진 PNG 이미지 렌더링 (대문자 -O):

`osage -T {{png}} -O {{경로/대상/입력.gv}}`

- 지정된 출력 파일 이름으로 SVG 이미지 렌더링 (소문자 -o):

`osage -T {{svg}} -o {{경로/대상/이미지.svg}} {{경로/대상/입력.gv}}`

- PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON, 또는 DOT 형식으로 출력 렌더링:

`osage -T {{형식}} -O {{경로/대상/입력.gv}}`

- `stdin`과 `stdout`을 사용하여 GIF 이미지 렌더링:

`echo "{{digraph {this -> that} }}" | osage -T {{gif}} > {{경로/대상/이미지.gif}}`

- 도움말 표시:

`osage -?`
