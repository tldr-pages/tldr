# maim

> 스크린샷 유틸리티.
> 더 많은 정보: <https://github.com/naelstrof/maim>.

- 스크린샷을 캡처하여 지정된 경로에 저장:

`maim {{경로/대상/스크린샷.png}}`

- 선택한 영역의 스크린샷 캡처:

`maim --select {{경로/대상/스크린샷.png}}`

- 선택한 영역의 스크린샷을 캡처하여 클립보드에 저장 (`xclip` 필요):

`maim --select | xclip -selection clipboard -target image/png`

- 현재 활성 창의 스크린샷 캡처 (`xdotool` 필요):

`maim --window $(xdotool getactivewindow) {{경로/대상/스크린샷.png}}`
