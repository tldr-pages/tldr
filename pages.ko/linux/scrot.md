# scrot

> 스크린 캡처 유틸리티.
> 더 많은 정보: <https://github.com/resurrecting-open-source-projects/scrot>.

- 스크린샷을 캡처하여 현재 디렉토리에 현재 날짜를 파일명으로 저장:

`scrot`

- 스크린샷을 캡처하여 `capture.png`로 저장:

`scrot {{capture.png}}`

- 대화형으로 스크린샷 캡처:

`scrot --select`

- 키보드 입력으로 종료하지 않고 대화형으로 스크린샷 캡처, `<Esc>`를 눌러 종료:

`scrot --select --ignorekeyboard`

- 색상이 있는 선으로 영역을 구분하여 대화형으로 스크린샷 캡처:

`scrot --select --line color={{x11_색상|rgb_색상}}`

- 현재 포커스된 창에서 스크린샷 캡처:

`scrot --focused`

- 스크린샷을 찍기 전에 10초 카운트다운 표시:

`scrot --count --delay {{10}}`
