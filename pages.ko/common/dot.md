# dot

> `graphviz` 파일로부터 `선형 방향` 네트워크 그래프를 렌더링.
> 레이아웃: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage`, `patchwork`.
> 더 많은 정보: <https://graphviz.org/doc/info/command.html>.

- 입력 파일명과 출력 포맷에 기반한 파일명으로 PNG 이미지 렌더링(대문자 -O 사용):

`dot -T {{png}} -O {{경로/대상/입력_파일명.gv}}`

- 지정된 출력 파일명으로 SVG 이미지 렌더링(소문자 -o 사용):

`dot -T {{svg}} -o {{경로/대상/이미지.svg}} {{경로/대상/입력_파일명.gv}}`

- PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON, DOT 포맷으로 출력물을 렌더링:

`dot -T {{format}} -O {{경로/대상/입력_파일명.gv}}`

- `stdin`과 `stdout`을 사용해 GIF 이미지를 렌더링:

`echo "{{digraph {this -> that} }}" | dot -T {{gif}} > {{경로/대상/이미지.gif}}`

- 도움말을 표시:

`dot -?`
