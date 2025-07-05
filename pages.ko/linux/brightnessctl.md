# brightnessctl

> Linux 운영 체제에서 장치 밝기를 읽고 제어하는 유틸리티.
> 더 많은 정보: <https://github.com/Hummer12007/brightnessctl#usage>.

- 밝기를 변경할 수 있는 장치 나열:

`brightnessctl {{[-l|--list]}}`

- 디스플레이 백라이트의 현재 밝기 출력:

`brightnessctl get`

- 디스플레이 백라이트의 밝기를 지정된 범위 내의 백분율로 설정:

`brightnessctl set {{50%}}`

- 지정된 증가분만큼 밝기 증가:

`brightnessctl set {{+10%}}`

- 지정된 감소분만큼 밝기 감소:

`brightnessctl set {{10%-}}`
