# sha1sum

> SHA1 암호화 체크섬 계산.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/sha1sum>.

- 하나 이상의 파일에 대한 SHA1 체크섬 계산:

`sha1sum {{경로/대상/파일1 경로/대상/파일2 ...}}`

- SHA1 체크섬 목록을 파일에 계산 및 저장:

`sha1sum {{경로/대상/파일1 경로/대상/파일2 ...}} > {{경로/대상/파일.sha1}}`

- `stdin`에서 SHA1 체크섬 계산:

`{{명령어}} | sha1sum`

- SHA1 체크섬과 파일 이름 목록이 포함된 파일을 읽어 모든 파일이 일치하는지 검증:

`sha1sum --check {{경로/대상/파일.sha1}}`

- 누락된 파일 또는 검증 실패 시에만 메시지 표시:

`sha1sum --check --quiet {{경로/대상/파일.sha1}}`

- 누락된 파일은 무시하고 검증 실패 시에만 메시지 표시:

`sha1sum --ignore-missing --check --quiet {{경로/대상/파일.sha1}}`
