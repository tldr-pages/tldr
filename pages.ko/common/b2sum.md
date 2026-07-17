# b2sum

> BLACK2 암호화 체크섬을 계산.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>.

- 하나 이상의 파일에 대해 BLAKE2 체크섬을 계산:

`b2sum {{경로/대상/파일1 경로/대상/파일2 ...}}`

- BLAKE2 체크섬 목록을 계산하고 파일에 저장:

`b2sum {{경로/대상/파일1 경로/대상/파일2 ...}} > {{경로/대상/파일.b2}}`

- `stdin`에서 BLAKE2 체크섬을 계산:

`{{command}} | b2sum`

- BLAKE2 합계 및 파일이름의 파일을 읽고 모든 파일에 일치하는 체크섬을 확인:

`b2sum --check {{경로/대상/파일.b2}}`

- 누락된 파일이 있거나 확인에 실패한 경우에만 메시지를 표시:

`b2sum --check --quiet {{경로/대상/파일.b2}}`

- 누락된 파일은 무시하고, 확인에 실패한 경우에만 메시지를 표시:

`b2sum --ignore-missing --check --quiet {{경로/대상/파일.b2}}`
