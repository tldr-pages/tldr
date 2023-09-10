# aws cloudwatch

> AWS 리소스를 모니터링하여 리소스 이용률, 애플리케이션 성능 및 운영 상태에 대한 시스템 전반적인 가시성 확보.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html>.

- 대시보드 목록 나열:

`aws cloudwatch list-dashboards`

- 지정한 대시보드의 세부 정보 표시:

`aws cloudwatch get-dashboard --dashboard-name {{대시보드_이름}}`

- 메트릭 목록 나열:

`aws cloudwatch list-metrics`

- 알람(경보) 목록 나열:

`aws cloudwatch describe-alarms`

- 해당 매트릭과 연결된 알람 생성(또는 업데이트):

`aws cloudwatch put-metric-alarm --alarm-name {{알람_이름}} --evaluation-periods {{평가_주기}} --comparison-operator {{비교_연산자}}`

- 지정한 알람들 삭제:

`aws cloudwatch delete-alarms --alarm_names {{알람_이름}}`

- 지정한 대시보드들 삭제:

`aws cloudwatch delete-dashboards --dashboard-names {{대시보드_이름}}`
