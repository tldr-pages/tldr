# xclock

> 아날로그 또는 디지털 형태로 시간을 표시합니다.
> 더 많은 정보: <https://manned.org/xclock>.

- 아날로그 시계 표시:

`xclock`

- 시와 분 필드만 있는 24시간 디지털 시계 표시:

`xclock -digital -brief`

- strftime 형식 문자열을 사용하여 디지털 시계 표시 (strftime(3) 참조):

`xclock -digital -strftime {{형식}}`

- 매 초 업데이트되는 시, 분, 초 필드가 있는 24시간 디지털 시계 표시:

`xclock -digital -strftime '%H:%M:%S' -update 1`

- 시와 분 필드만 있는 12시간 디지털 시계 표시:

`xclock -digital -twelve -brief`
