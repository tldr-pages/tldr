# date

> 시스템 날짜 설정 및 표시.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/date>.

- 기본 로컬 형식을 사용하여 현재 날짜 표시:

`date +%c`

- 현재 날짜를 UTC 및 ISO 8601 형식으로 표시:

`date -u +%Y-%m-%dT%H:%M:%S%Z`

- 현재 날짜를 Unix 타임스탬프로 표시 (Unix epoch 이후 몇 초):

`date +%s`

- 기본 형식을 사용하여 특정 날짜 표시(Unix 타임스탬프로 표시):

`date -d @{{1473305798}}`

- 특정 날짜를 Unix 타임스탬프 형식으로 변환:

`date -d "{{2018-09-01 00:00}}" +%s --utc`

- 현재 날짜를 RFC-3339 형식으로 표시 (`YYYY-MM-DD hh:mm:ss TZ`):

`date --rfc-3339=s`

- `MMDDhhmmYYYY.ss` (`YYYY` 와 `.ss`는 선택 사항) 형식을 사용해 현재 날짜를 설정:

`date {{093023592021.59}}`

- ISO 기준 현재 몇 번째 주인지 표시:

`date +%V`
