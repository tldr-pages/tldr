# cat

> [f]파일을 출력하고 연결.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>.

- [f]파일의 내용을 `stdout`에 출력:

`cat {{경로/대상/파일}}`

- 여러 [f]파일을 연결하여 출력 [f]파일로 저장:

`cat {{경로/대상/파일1 경로/대상/파일2 ...}} > {{경로/대상/출력_파일}}`

- 여러 [f]파일을 출력 [f]파일에 추가:

`cat {{경로/대상/파일1 경로/대상/파일2 ...}} >> {{경로/대상/출력_파일}}`

- `stdin`을 [f]파일로 작성:

`cat - > {{경로/대상/파일}}`

- 모든 출력 줄에 [n]번호 추가:

`cat {{[-n|--number]}} {{경로/대상/파일}}`

- 비인쇄 및 공백 문자를 표시 (비ASCII의 경우 `M-` 접두사 사용):

`cat {{[-vte|--show-nonprinting -t -e]}} {{경로/대상/파일}}`
