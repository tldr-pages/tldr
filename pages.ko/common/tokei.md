# tokei

> 코드에 대한 통계 표시.
> 더 많은 정보: <https://github.com/XAMPPRocky/tokei>.

- 디렉토리 및 모든 하위 디렉토리의 코드에 대한 보고서 표시:

`tokei {{경로/대상/폴더}}`

- `.min.js` 파일을 제외한 디렉토리의 보고서 표시:

`tokei {{경로/대상/폴더}} -e {{*.min.js}}`

- 디렉토리 내 개별 파일에 대한 통계 표시:

`tokei {{경로/대상/폴더}} --files`

- Rust 및 Markdown 유형의 모든 파일에 대한 보고서 표시:

`tokei {{경로/대상/폴더}} -t={{Rust}},{{Markdown}}`
