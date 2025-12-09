# cam

> `libcamera`의 프론트엔드 도구.
> 더 많은 정보: <https://libcamera.org/docs.html>.

- 사용 가능한 카메라 나열:

`cam {{[-l|--list]}}`

- 카메라의 컨트롤 나열:

`cam {{[-c|--camera]}} {{카메라_인덱스}} --list-controls`

- 프레임을 폴더에 저장:

`cam {{[-c|--camera]}} {{카메라_인덱스}} {{[-C|--capture=]}}{{캡처할_프레임_수}} {{[-F|--file]}}`

- 창에 카메라 피드 표시:

`cam {{[-c|--camera]}} {{카메라_인덱스}} {{[-C|--capture]}} {{[-S|--sdl]}}`
