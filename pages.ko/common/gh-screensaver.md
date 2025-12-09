# gh screensaver

> GitHub CLI용 확장 기능으로 애니메이션 터미널 화면 보호기를 실행합니다.
> 같이 보기: `gh extension`.
> 더 많은 정보: <https://github.com/vilmibm/gh-screensaver>.

- 무작위 화면 보호기 실행:

`gh screensaver`

- 특정 화면 보호기 실행:

`gh screensaver --saver {{fireworks|life|marquee|pipes|pollock|starfield}}`

- 특정 텍스트와 폰트를 사용하여 "marquee" 화면 보호기 실행:

`gh screensaver --saver {{marquee}} -- --message="{{메시지}}" --font={{폰트_이름}}`

- 특정 밀도와 속도로 "starfield" 화면 보호기 실행:

`gh screensaver --saver {{starfield}} -- --density {{500}} --speed {{10}}`

- 사용 가능한 화면 보호기 목록 나열:

`gh screensaver --list`
