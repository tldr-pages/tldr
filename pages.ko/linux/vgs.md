# vgs

> 볼륨 그룹에 대한 정보를 표시합니다.
> 관련 항목: `lvm`.
> 더 많은 정보: <https://manned.org/vgs>.

- 볼륨 그룹에 대한 정보 표시:

`sudo vgs`

- 모든 볼륨 그룹 표시:

`sudo vgs {{[-a|--all]}}`

- 기본 표시 항목을 더 자세히 보이도록 변경:

`sudo vgs {{[-v|--verbose]}}`

- 특정 필드만 표시:

`sudo vgs {{[-o|--options]}} {{필드_이름_1,필드_이름_2,...}}`

- 기본 표시 항목에 필드를 추가:

`sudo vgs {{[-o|--options]}} +{{필드_이름}}`

- 제목 줄을 생략:

`sudo vgs --noheadings`

- 필드를 구분자와 함께 구분하여 사용:

`sudo vgs --separator =`
