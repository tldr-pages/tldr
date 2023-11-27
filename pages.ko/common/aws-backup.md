# aws backup

> Amazon Web Services와 관련 데이터를 보호하기 위해 설계된 통합 백업 서비스.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

- 특정 BackupPlanId에 대한 백업 계획 세부 정보 반환:

`aws backup get-backup-plan --backup-plan-id {{id}}`

- 특정 백업 계획 이름과 백업 규칙을 사용해 백업 계획 생성:

`aws backup create-backup-plan --backup-plan {{plan}}`

- 특정 백업 계획 삭제:

`aws backup delete-backup-plan --backup-plan-id {{id}}`

- 현재 계정에 대한 모든 활성 백업 계획 목록 반환:

`aws backup list-backup-plans`

- 보고서 작업에 대한 세부 정보 표시:

`aws backup list-report-jobs`
