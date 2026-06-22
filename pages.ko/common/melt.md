# melt

> 기억하기 쉬운 시드 문구를 사용하여 Ed25519 SSH 키 백업 및 복원.
> 더 많은 정보: <https://github.com/charmbracelet/melt#usage>.

- 기존 Ed25519 개인 키로부터 시드 문구 생성:

`melt {{~/.ssh/id_ed25519}}`

- 표준 입력(`stdin`)으로 전달된 Ed25519 키로부터 시드 문구 생성:

`{{cat ~/.ssh/id_ed25519}} | melt`

- 시드 문구를 사용하여 SSH 키 복원:

`melt restore {{경로/대상/키}} --seed "{{시드_문구}}"`

- 표준 입력(`stdin`)으로 전달된 시드 문구를 사용하여 SSH 키 복원:

`{{cat 경로/대상/파일}} | melt restore -`
