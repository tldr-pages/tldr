# openscad

> 솔리드 3D CAD 객체를 생성하는 소프트웨어.
> 더 많은 정보: <https://manned.org/openscad>.

- 파일 열기:

`openscad {{경로/대상/button.scad}}`

- 파일을 STL로 변환:

`openscad -o {{경로/대상/button.stl}} {{경로/대상/button.scad}}`

- 특정 색 구성표로 파일을 PNG로 렌더링:

`openscad -o {{경로/대상/button.png}} --colorscheme {{Sunset}} {{경로/대상/button.scad}}`
