# slurp

> Wayland 컴포지터에서 영역을 선택.
> 더 많은 정보: <https://github.com/emersion/slurp/blob/master/slurp.1.scd>.

- 영역을 선택하고 `stdout`에 출력:

`slurp`

- 영역을 선택하고 선택한 영역의 크기를 표시하면서 `stdout`에 출력:

`slurp -d`

- 영역 대신 단일 지점 선택:

`slurp -p`

- 출력물을 선택하고 그 이름을 출력:

`slurp -o -f '%o'`

- 특정 영역을 선택하고 `grim`을 사용하여 테두리가 없는 스크린샷 찍기:

`grim -g "$(slurp -w 0)"`

- 특정 영역을 선택하고 `wf-recorder`를 사용하여 테두리가 없는 비디오 촬영:

`wf-recorder --geometry "$(slurp -w 0)"`
