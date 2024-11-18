# i3-scrot

> i3 윈도우 관리자를 위한 스크린샷 유틸리티 `scrot`의 래퍼 스크립트.
> 기본 저장 위치는 `~/Pictures`이며, `~/.config/i3-scrot.conf`에서 변경할 수 있습니다.
> 더 많은 정보: <https://gitlab.manjaro.org/packages/community/i3/i3-scrot>.

- 전체 화면의 스크린샷을 캡처하여 기본 디렉토리에 저장:

`i3-scrot`

- 활성 창의 스크린샷 캡처:

`i3-scrot --window`

- 특정 사각형 영역의 스크린샷 캡처:

`i3-scrot --select`

- 전체 화면의 스크린샷을 캡처하여 클립보드로 복사:

`i3-scrot --desk-to-clipboard`

- 활성 창의 스크린샷을 캡처하여 클립보드로 복사:

`i3-scrot --window-to-clipboard`

- 특정 영역의 스크린샷을 캡처하여 클립보드로 복사:

`i3-scrot --select-to-clipboard`

- 5초 후 활성 창의 스크린샷 캡처:

`i3-scrot --window {{5}}`
