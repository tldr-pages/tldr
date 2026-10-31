# dysk

> 파일 시스템 정보를 표 형식으로 표시합니다.
> 더 많은 정보: <https://manned.org/dysk>.

- 일반 디스크에 대한 표준 개요 확인:

`dysk`

- 여유 크기로 정렬:

`dysk {{[-s|--sort]}} free`

- HDD 디스크만 포함:

`dysk {{[-f|--filter]}} 'disk = HDD'`

- SSD 디스크 제외:

`dysk {{[-f|--filter]}} 'disk <> SSD'`

- 높은 사용률 또는 낮은 여유 공간을 가진 디스크 표시:

`dysk {{[-f|--filter]}} 'use > 65% | free < 50G'`
