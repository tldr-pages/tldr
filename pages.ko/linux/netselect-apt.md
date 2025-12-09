# netselect-apt

> 지연 시간이 가장 낮은 Debian 미러를 위한 `sources.list` 파일 생성.
> 더 많은 정보: <https://manned.org/netselect-apt>.

- 가장 낮은 지연 시간의 서버를 사용하여 `sources.list` 생성:

`sudo netselect-apt`

- Debian 브랜치를 지정, 기본적으로 stable이 사용됨:

`sudo netselect-apt {{testing}}`

- non-free 섹션 포함:

`sudo netselect-apt --non-free`

- 미러 목록 조회를 위한 국가 지정:

`sudo netselect-apt -c {{인도}}`
