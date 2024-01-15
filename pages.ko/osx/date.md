# date

> 시스템 날짜 설정 또는 표시.
> 더 많은 정보: <https://ss64.com/osx/date.html>.

- 기본 로케일 형식을 사용하여 현재 날짜를 표시:

`date +%c`

- 현재 날짜를 UTC 및 ISO 8601 형식으로 표시:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- 현재 날짜를 Unix 타임스탬프(Unix 간격 이후초)로 표시:

`date +%s`

- 기본 형식을 사용하여 특정 날짜(Unix 타임스탬프로 표시) 표시:

`date -r 1473305798`
