# gh gpg-key

> 인증된 GitHub 계정에 등록된 GPG 키 관리.
> 관련 항목: `gpg`.
> 더 많은 정보: <https://cli.github.com/manual/gh_gpg-key>.

- 인증된 GitHub 계정의 GPG 키 목록 표시:

`gh gpg-key {{[ls|list]}}`

- 키 파일을 지정하여 GitHub 계정에 GPG 키 추가:

`gh gpg-key add {{경로/대상/키_파일}}`

- 키 ID를 지정하여 인증된 GitHub 계정에 GPG 키 추가:

`gpg {{[-a|--armor]}} --export {{키_아이디}} | gh gpg-key add -`

- 인증된 GitHub 계정에서 GPG 키 삭제:

`gh gpg-key delete {{키_아이디}}`
