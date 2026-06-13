# colorpicker

> 최소화된 X11 색상선택기.
> 왼쪽 클릭을 제외한 모든 마우스 동작은 프로그램을 종료.
> 더 많은 정보: <https://github.com/ym1234/colorpicker>.

- 색상 선택기를 실행하고 클릭한 각 픽셀의 16진수 및 RGB 값을 `stdout`로 출력:

`colorpicker`

- 클릭한 픽셀 하나의 색상만 출력하고 종료:

`colorpicker --one-shot`

- 클릭한 각 픽셀의 색상을 출력하고 키를 누르면 종료:

`colorpicker --quit-on-keypress`

- RGB 값만 출력:

`colorpicker --rgb`

- 16진수 값만 출력:

`colorpicker --hex`
