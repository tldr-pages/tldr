# sed

> 스크립트 방식으로 텍스트를 편집합니다.
> 같이 보기: `awk`, `ed`.
> 더 많은 정보: <https://www.gnu.org/software/sed/manual/sed.html>.

- 모든 입력 줄에서 `apple` (기본 정규식) 발생 부분을 `mango` (기본 정규식)로 대체하고 결과를 `stdout`에 출력:

`{{command}} | sed 's/apple/mango/g'`

- 모든 입력 줄에서 `apple` (확장 정규식) 발생 부분을 `APPLE` (확장 정규식)로 대체하고 결과를 `stdout`에 출력:

`{{command}} | sed {{[-E|--regexp-extended]}} 's/(apple)/\U\1/g'`

- 특정 파일에서 모든 `apple` (기본 정규식) 발생 부분을 `mango` (기본 정규식)로 대체하고 원본 파일을 직접 덮어쓰기:

`sed {{[-i|--in-place]}} 's/apple/mango/g' {{경로/대상/파일}}`

- 특정 스크립트 파일을 실행하고 결과를 `stdout`에 출력:

`{{command}} | sed {{[-f|--file]}} {{경로/대상/스크립트.sed}}`

- 첫 번째 줄만 `stdout`에 출력:

`{{command}} | sed {{[-n|--quiet]}} '1p'`

- 파일의 첫 번째 줄 삭제:

`sed {{[-i|--in-place]}} 1d {{경로/대상/파일}}`

- 파일의 첫 번째 줄에 새 줄 삽입:

`sed {{[-i|--in-place]}} '1i\your new line text\' {{경로/대상/파일}}`
