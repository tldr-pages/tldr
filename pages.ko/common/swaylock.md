# swaylock

> Wayland 컴포지터용 화면 잠금 도구.
> 더 많은 정보: <https://manned.org/swaylock>.

- 흰색 배경으로 화면 잠금:

`swaylock`

- 단색 배경으로 화면 잠금 (rrggbb 형식):

`swaylock --color {{0000ff}}`

- PNG 배경 이미지로 화면 잠금:

`swaylock --image {{경로/대상/파일.png}}`

- 잠금 해제 표시기를 비활성화하고 화면 잠금 (키 입력 시 피드백 제거):

`swaylock --no-unlock-indicator`

- 모든 모니터에 타일 형식으로 PNG 배경 이미지로 화면 잠금:

`swaylock --image {{경로/대상/파일.png}} --tiling`

- 실패한 로그인 시도 횟수를 표시하며 화면 잠금:

`swaylock --show-failed-attempts`

- 파일에서 설정 불러오기:

`swaylock --config {{경로/대상/설정}}`
