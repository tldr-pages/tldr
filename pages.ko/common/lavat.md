# lavat

> 터미널에 애니메이션 용암 램프 효과를 표시.
> 색상, 속도, 크기, 움직임 및 표시 스타일 사용자 지정 가능.
> 더 많은 정보: <https://github.com/AngelJumbo/lavat#usage>.

- 기본 용암 애니메이션 시작:

`lavat`

- 이름 있는 lava 색상과 rim 색상ㅇ로 시작:

`lavat -c {{green}} -k {{red}}`

- 두 hex 색상을 사용하여 그라데이션 모드로 시작:

`lavat -g -c {{00FF00}} -k {{FF0000}}`

- 중력 및 부력 움직임 활성화:

`lavat -G`

- 속도, 반지름, 테두리 킄기, metaball 개수를 사용자 지정하여 시작:

`lavat -s {{1..10}} -r {{1..10}} -R {{1..5}} -b {{5..20}}`

- 사용자 지정 ASCII 문자 집합으로 시작:

`lavat -F "{{.oO@}}"`

- 도움말 표시:

`lavat -h`
