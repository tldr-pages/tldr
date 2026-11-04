# cliphist

> Wayland 컴포지터의 클립보드 기록을 관리.
> `wl-copy` 및 `wl-paste`와 함께 사용됨.
> 더 많은 정보: <https://github.com/sentriz/cliphist#usage>.

- 클립보드 기록 목록 표시:

`cliphist list`

- 이전 클립보드 항목을 선택하여 다시 복사 (`fzf` 사용):

`cliphist list | fzf | cliphist decode | wl-copy`

- 저장된 모든 클립보드 기록 삭제:

`cliphist wipe`

- 지정한 ID의 클립보드 기록 삭제:

`cliphist delete {{아이디}}`

- 현재 클립보드 내용을 수동으로 저장:

`wl-paste | cliphist store`
