# tex-fmt

> LaTeX 소스 코드를 포맷.
> 더 많은 정보: <https://github.com/WGUNDERWOOD/tex-fmt>.

- 파일을 포맷하고, 원본 파일을 덮어쓰기:

`tex-fmt {{경로/대상/파일.tex}}`

- 파일이 올바르게 포맷되어 있는지 검사:

`tex-fmt --check {{경로/대상/파일.tex}}`

- `stdin`에서 파일을 읽어 포맷하고 결과를 `stdout`으로 출력:

`cat {{경로/대상/파일.tex}} | tex-fmt --stdin`
