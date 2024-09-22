# aws rds

> 관계형 데이터베이스를 설정, 운영 및 확장하기 위한 웹 서비스인 AWS Relational Database Service를 사용.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html>.

- 특정 RDS 하위 명령어에 대한 도움말을 표시:

`aws rds {{하위명령어}} help`

- 인스턴스 중지:

`aws rds stop-db-instance --db-instance-identifier {{인스턴스_구분자}}`

- 인스턴스 시작:

`aws rds start-db-instance --db-instance-identifier {{인스턴스_구분자}}`

- RDS 인스턴스 수정:

`aws rds modify-db-instance --db-instance-identifier {{인스턴스_구분자}} {{매개변수}} --apply-immediately`

- RDS 인스턴스에 업데이트 적용:

`aws rds apply-pending-maintenance-action --resource-identifier {{database_arn}} --apply-action {{system-update}} --opt-in-type {{immediate}}`

- 인스턴스 구분자 변경:

`aws rds modify-db-instance --db-instance-identifier {{오래된_인스턴스_구분자}} --new-db-instance-identifier {{새로운_인스턴스_구분자}}`

- 인스턴스 재부팅:

`aws rds reboot-db-instance --db-instance-identifier {{인스턴스_구분자}}`

- 인스턴스 삭제:

`aws rds delete-db-instance --db-instance-identifier {{인스턴스_구분자}} --final-db-snapshot-identifier {{스냅샷_구분자}} --delete-automated-backups`
