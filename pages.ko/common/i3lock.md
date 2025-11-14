# i3lock

> i3 윈도우 관리자를 위해 만들어진 간단한 화면 잠금 도구.
> 더 많은 정보: <https://manned.org/i3lock>.

- 흰색 배경으로 화면 잠금:

`i3lock`

- 단색 배경(rrggbb 형식)으로 화면 잠금:

`i3lock --color {{0000ff}}`

- PNG 배경으로 화면 잠금:

`i3lock --image {{경로/대상/파일.png}}`

- 잠금 해제 표시기를 비활성화하고 화면 잠금 (키 입력 시 피드백 제거):

`i3lock --no-unlock-indicator`

- 마우스 포인터를 숨기지 않고 화면 잠금:

`i3lock --pointer {{default}}`

- 모든 모니터에 타일링된 PNG 배경으로 화면 잠금:

`i3lock --image {{경로/대상/파일.png}} --tiling`

- 실패한 로그인 시도 횟수를 표시하며 화면 잠금:

`i3lock --show-failed-attempts`
