# aurvote

> Arch User Repository의 패키지에 투표합니다.
> 투표를 하려면 `~/.config/aurvote` 파일이 존재하고 AUR 자격 증명이 포함되어 있어야 합니다.
> 더 많은 정보: <https://github.com/archlinuxfr/aurvote#name>.

- 대화형으로 AUR 사용자명과 비밀번호를 포함한 `~/.config/aurvote` 파일 생성:

`aurvote --configure`

- 하나 이상의 AUR 패키지에 투표:

`aurvote {{패키지1 패키지2 ...}}`

- 하나 이상의 AUR 패키지에서 투표 취소:

`aurvote --unvote {{패키지1 패키지2 ...}}`

- 하나 이상의 AUR 패키지가 이미 투표되었는지 확인:

`aurvote --check {{패키지1 패키지2 ...}}`

- 도움말 표시:

`aurvote --help`
