# sha256sum

> SHA256 암호화 체크섬 계산.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- 하나 이상의 파일에 대한 SHA256 체크섬 계산:

`sha256sum {{경로/대상/파일1 경로/대상/파일2 ...}}`

- SHA256 체크섬 목록을 파일에 계산 및 저장:

`sha256sum {{경로/대상/파일1 경로/대상/파일2 ...}} > {{경로/대상/파일.sha256}}`

- `stdin`에서 SHA256 체크섬 계산:

`{{명령어}} | sha256sum`

- SHA256 체크섬과 파일 이름 목록이 포함된 파일을 읽어 모든 파일이 일치하는지 검증:

`sha256sum --check {{경로/대상/파일.sha256}}`

- 누락된 파일 또는 검증 실패 시에만 메시지 표시:

`sha256sum --check --quiet {{경로/대상/파일.sha256}}`

- 누락된 파일은 무시하고 검증 실패 시에만 메시지 표시:

`sha256sum --ignore-missing --check --quiet {{경로/대상/파일.sha256}}`
