# xev

> X 이벤트의 내용을 출력.
> 더 많은 정보: <https://gitlab.freedesktop.org/xorg/app/xev>.

- 발생하는 모든 X 이벤트 모니터링:

`xev`

- 새 창을 생성하지 않고 루트 창의 모든 X 이벤트 모니터링:

`xev -root`

- 특정 창의 모든 X 이벤트 모니터링:

`xev -id {{창_ID}}`

- 주어진 카테고리의 X 이벤트 모니터링 (여러 번 지정 가능):

`xev -event {{이벤트_카테고리}}`
