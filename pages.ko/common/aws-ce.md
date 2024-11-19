# aws ce

> AWS Cost Explorer 서비스를 통한 비용 관리 작업 수행합니다.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html>.

- 이상 모니터 생성:

`aws ce create-anomaly-monitor --monitor {{모니터_이름}} --monitor-type {{모니터_유형}}`

- 이상 구독 생성:

`aws ce create-anomaly-subscription --subscription {{구독_이름}} --monitor-arn {{모니터_arn}} --subscribers {{구독자}}`

- 이상 조회:

`aws ce get-anomalies --monitor-arn {{모니터_arn}} --start-time {{시작_날짜}} --end-time {{종료_날짜}}`

- 비용 및 사용량 조회:

`aws ce get-cost-and-usage --time-period {{시작_날짜}}/{{종료_날짜}} --granularity {{세분화}} --metrics {{메트릭}}`

- 비용 예측 조회:

`aws ce get-cost-forecast --time-period {{시작_날짜}}/{{종료_날짜}} --granularity {{세분화}} --metric {{메트릭}}`

- 예약 사용량 조회:

`aws ce get-reservation-utilization --time-period {{시작_날짜}}/{{종료_날짜}} --granularity {{세분화}}`

- 비용 카테고리 정의 목록 조회:

`aws ce list-cost-category-definitions`

- 리소스 태깅:

`aws ce tag-resource --resource-arn {{리소스_arn}} --tags {{태그}}`
