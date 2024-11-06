# stl2gts

> STL 파일을 GTS(GNU 삼각형 표면 라이브러리) 파일 형식으로 변환.
> 더 많은 정보: <https://manned.org/stl2gts>.

- STL 파일을 GTS 파일로 변환:

`stl2gts < {{경로/대상/파일.stl}} > {{경로/대상/파일.gts}}`

- STL 파일을 GTS 파일로 변환하고 면의 법선을 뒤집기:

`stl2gts --revert < {{경로/대상/파일.stl}} > {{경로/대상/파일.gts}}`

- STL 파일을 GTS 파일로 변환하고 정점 병합 안 함:

`stl2gts --nomerge < {{경로/대상/파일.stl}} > {{경로/대상/파일.gts}}`

- STL 파일을 GTS 파일로 변환하고 표면 통계 표시:

`stl2gts --verbose < {{경로/대상/파일.stl}} > {{경로/대상/파일.gts}}`

- 도움말 표시:

`stl2gts --help`
