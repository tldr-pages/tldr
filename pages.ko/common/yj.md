# yj

> 맵 순서를 유지하면서 YAML, TOML, JSON, HCL 형식 간 변환을 수행.
> 더 많은 정보: <https://github.com/sclevine/yj>.

- `stdin`에서 [y]AML을 읽어 JSON (기본값)으로 변환하고 결과를 `stdout`에 출력:

`yj < {{파일.yml}} -y`

- [t]OML을 [y]AML로 변환:

`yj < {{파일.toml}} -ty`

- [j]SON을 [t]OML로 변환하고 들여쓰기([i]ndentation) 적용:

`yj < {{파일.json}} -jti`

- H[c]L을 [j]SON으로 변환:

`yj < {{파일.hcl}} -cj`

- inf/[n]aN 변환을 무시하고 [y]AML을 H[c]L로 변환:

`yj < {{파일.yml}} -ycn`

- 버전([v]ersion) 정보 표시:

`yj -v`
