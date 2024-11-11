# cam

> `libcamera`의 프론트엔드 도구.
> 더 많은 정보: <https://libcamera.org/docs.html>.

- 사용 가능한 카메라 나열:

`cam --list`

- 카메라의 컨트롤 나열:

`cam --camera {{카메라_인덱스}} --list-controls`

- 프레임을 폴더에 저장:

`cam --camera {{카메라_인덱스}} --capture={{캡처할_프레임_수}} --file`

- 창에 카메라 피드 표시:

`cam --camera {{카메라_인덱스}} --capture --sdl`
