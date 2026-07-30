# grabc

> X Window의 픽셀 색상을 확인하는 도구.
> 더 많은 정보: <https://manned.org/grabc>.

- 픽셀을 선택하고 색상을 16진수로 출력:

`grabc`

- 픽셀을 선택하고 RGB 값 출력:

`grabc -rgb`

- 디버그 메시지 활성화:

`grabc -d`

- 클릭한 창의 16진수 ID 출력:

`grabc -W`

- 지정한 창의 특정 위치에 있는 픽셀 색상 선택:

`grabc -w {{윈도우_아이디}} -l +{{x}}+{{y}}`

- 색상의 전체 16비트 값 출력 (기본값은 상위 8비트만 출력):

`grabc -a`

- 도움말 표시:

`grabc -h`
