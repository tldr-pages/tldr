# md-to-clip

> tldr 페이지를 커맨드라인 인터페이스 페이지로 변환.
> 같이 보기: `clip-view`.
> 더 많은 정보: <https://github.com/command-line-interface-pages/v2-tooling/tree/main/md-to-clip>.

- tldr 페이지 파일을 변환하고 같은 디렉토리에 저장:

`md-to-clip {{경로/대상/페이지.md 경로/대상/페이지2.md ...}}`

- tldr 페이지 파일을 변환하고 특정 디렉토리에 저장:

`md-to-clip --output-directory {{경로/대상/폴더}} {{경로/대상/페이지1.md 경로/대상/페이지2.md ...}}`

- tldr 페이지 파일을 변환하여 `stdout`에 출력:

`md-to-clip --no-file-save <(echo '{{페이지-내용}}')`

- 특정 설정 파일에서 추가 플레이스홀더를 인식하여 tldr 페이지 파일 변환:

`md-to-clip --special-placeholder-config {{경로/대상/구성.yaml}} {{경로/대상/페이지1.md 경로/대상/페이지2.md ...}}`

- 도움말 표시:

`md-to-clip --help`

- 버전 정보 표시:

`md-to-clip --version`
