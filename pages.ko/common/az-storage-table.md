# az storage table

> Azure에서 NoSQL 키-값 스토리지를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/storage/table>.

- 스토리지 계정에 새 테이블을 만듬:

`az storage table create --account-name {{스토리지_계정_이름}} --name {{테이블_이름}} --fail-on-exist`

- 테이블에 대한 공유 액세스 서명을 공유:

`az storage table generate-sas --account-name {{스토리지_계정_이름}} --name {{테이블_이름}} --permissions {{sas_permissions}} --expiry {{만료_날짜}} --https-only`

- 스토리지 계정의 테이블 나열:

`az storage table list --account-name {{스토리지_계정_이름}}`

- 지정된 테이블과 여기에 포함된 모든 데이터를 삭제:

`az storage table delete --account-name {{스토리지_계정_이름}} --name {{테이블_이름}} --fail-not-exist`
