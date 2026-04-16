# dunst

> X11 및 Wayland용 경량, 커스터마이즈 가능한 알림 데몬.
> 수동으로 시작하지 않으면, 알림이 전송될 때 D-Bus가 자동으로 `dunst`를 실행.
> 더 많은 정보: <https://dunst-project.org/documentation/dunst/>.

- `dunst` 실행:

`dunst`

- 시작 시 알림 표시:

`dunst -startup_notification`

- 수신된 알림을 `stdout`으로 출력:

`dunst -print`

- 지정한 설정 파일 사용 (기본값: `$XDG_CONFIG_HOME/dunst/dunstrc`):

`dunst {{[-conf|-config]}} {{경로/대상/파일}}`
