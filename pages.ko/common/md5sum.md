# md5sum

> MD5 암호화 체크섬 계산.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/md5sum-invocation.html>.

- 하나 이상의 파일에 대한 MD5 체크섬 계산:

`md5sum {{경로/대상/파일1 경로/대상/파일2 ...}}`

- MD5 체크섬 목록을 파일에 계산하고 저장:

`md5sum {{경로/대상/파일1 경로/대상/파일2 ...}} > {{경로/대상/파일.md5}}`

- `stdin`에서 MD5 체크섬 계산:

`{{명령어}} | md5sum`

- MD5 합 및 파일 이름이 포함된 파일을 읽고 모든 파일이 일치하는지 확인:

`md5sum --check {{경로/대상/파일.md5}}`

- 누락된 파일이나 확인 실패 시 메시지만 표시:

`md5sum --check --quiet {{경로/대상/파일.md5}}`

- 누락된 파일은 무시하고 확인 실패 시 메시지만 표시:

`md5sum --ignore-missing --check --quiet {{경로/대상/파일.md5}}`
