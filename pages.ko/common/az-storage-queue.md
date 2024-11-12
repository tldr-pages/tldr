# az storage queue

> Azure에서 스토리지 큐를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/storage/queue>.

- 큐 생성:

`az storage queue create --account-name {{스토리지_계정_이름}} --name {{큐_이름}} --metadata {{큐_메타데이터}}`

- 큐에 대한 공유 액세스 서명을 생성:

`az storage queue generate-sas --account-name {{스토리지_계정_이름}} --name {{큐_이름}} --permissions {{큐_권한}} --expiry {{만료_날짜}} --https-only`

- 스토리지 계정의 큐 나열:

`az storage queue list --prefix {{필터_접두사}} --account-name {{스토리지_계정_이름}}`

- 지정된 대기열과 포함된 모든 메시지를 삭제:

`az storage queue delete --account-name {{스토리지_계정_이름}} --name {{큐_이름}} --fail-not-exist`
