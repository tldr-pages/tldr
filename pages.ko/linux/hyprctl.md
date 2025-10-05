# hyprctl

> Hyprland Wayland 컴포지터의 일부를 제어.
> 더 많은 정보: <https://wiki.hypr.land/Configuring/Using-hyprctl/>.

- Hyprland 구성 파일 다시 로드:

`hyprctl reload`

- 활성 창 이름 반환:

`hyprctl activewindow`

- 연결된 입력 장치 모두 나열:

`hyprctl devices`

- 각 속성을 포함한 모든 출력 나열:

`hyprctl workspaces`

- 인수를 사용하여 디스패처 호출:

`hyprctl dispatch exec {{앱}}`

- 구성 키워드를 동적으로 설정:

`hyprctl keyword {{키워드}} {{값}}`

- 버전 표시:

`hyprctl version`
