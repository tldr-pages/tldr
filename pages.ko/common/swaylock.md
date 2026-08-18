# swaylock

> Wayland 컴포지터용 화면 잠금 도구.
> 더 많은 정보: <https://manned.org/swaylock>.

- `$HOME/.swaylock/config` 또는 `$XDG_CONFIG_HOME/swaylock/config`의 설정을 사용하여 화면 잠금:

`swaylock`

- 단색 배경으로 화면 잠금 (`rrggbb` 형식):

`swaylock {{[-c|--color]}} {{0000ff}}`

- 배경 이미지를 사용하여 화면 잠금:

`swaylock {{[-i|--image]}} {{경로/대상/이미지}}`

- 잠금 해제 표시기를 비활성화하고 화면 잠금 (키 입력 시 피드백 제거):

`swaylock {{[-u|--no-unlock-indicator]}}`

- 모든 모니터에 타일 형식으로 PNG 배경 이미지로 화면 잠금:

`swaylock {{[-i|--image]}} {{경로/대상/이미지}} {{[-t|--tiling]}}`

- 실패한 로그인 시도 횟수를 표시하며 화면 잠금:

`swaylock {{[-F|--show-failed-attempts]}}`

- 파일에서 설정 불러오기:

`swaylock {{[-C|--config]}} {{경로/대상/설정}}`
