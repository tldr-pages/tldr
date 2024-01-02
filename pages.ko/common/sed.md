# sed

> 스크립트 가능한 방식으로 텍스트 편집.
> 함께 보기: `awk`, `ed`.
> 더 많은 정보: <https://manned.org/man/sed.1posix>.

- 모든 입력 줄에서 모든 `apple`(기본 정규식)항목을 `mango`(기본 정규식)로 바꾸고 결과를 `stdout`에 출력:

`{{명령어}} | sed 's/apple/mango/g'`

- 특정 스크립트 파일([f]ile)을 실행하고 결과를 `stdout`에 출력:

`{{명령어}} | sed -f {{경로/대상/script.sed}}`

- `stdout`에 첫 번째 줄만 출력:

`{{명령어}} | sed -n '1p'`
