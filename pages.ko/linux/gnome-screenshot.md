# gnome-screenshot

> 화면, 창 또는 사용자 정의 영역을 캡처하고 이미지를 파일로 저장합니다.
> 더 많은 정보: <https://manned.org/gnome-screenshot>.

- 스크린샷을 찍고 기본 위치, 일반적으로 `~/Pictures`에 저장:

`gnome-screenshot`

- 스크린샷을 찍고 지정한 파일 위치에 저장:

`gnome-screenshot --file {{경로/대상/파일}}`

- 스크린샷을 찍고 클립보드에 저장:

`gnome-screenshot --clipboard`

- 지정한 초 후에 스크린샷 찍기:

`gnome-screenshot --delay {{5}}`

- GNOME Screenshot GUI 실행:

`gnome-screenshot --interactive`

- 현재 창의 스크린샷을 찍고 지정한 파일 위치에 저장:

`gnome-screenshot --window --file {{경로/대상/파일}}`

- 지정한 초 후에 스크린샷 찍고 클립보드에 저장:

`gnome-screenshot --delay {{10}} --clipboard`

- 버전 표시:

`gnome-screenshot --version`
