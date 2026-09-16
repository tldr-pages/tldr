# shpool

> 영구적으로 유지되는 쉘 세션을 생성하고 연결.
> 관련 항목: `tmux`, `screen`.
> 더 많은 정보: <https://github.com/shell-pool/shpool#usage>.

- 새로운 세션을 생성하거나 기존 세션에 연결:

`shpool attach {{세션_이름}}`

- 기존 세션 목록 표시:

`shpool list`

- 현재 세션에서 분리:

`shpool detach`

- 지정한 세션에서 분리:

`shpool detach {{세션_이름}}`

- 지정한 세션 종료:

`shpool kill {{세션_이름}}`

- `shpool` 데몬 시작ㅋ:

`shpool daemon`
