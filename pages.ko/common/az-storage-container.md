# az storage container

> Azure에서 blob 저장소 컨테이너를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/storage/container>.

- 스토리지 계정에 컨테이너를 생성:

`az storage container create --account-name {{스토리지_계정_이름}} --name {{컨테이너_이름}} --public-access {{접근_레벨}} --fail-on-exist`

- 컨테이너에 대한 공유 액세스 서명을 생성:

`az storage container generate-sas --account-name {{스토리지_계정_이름}} --name {{컨테이너_이름}} --permissions {{sas_permissions}} --expiry {{만료_날짜}} --https-only`

- 스토리지 계정의 컨테이너를 나열:

`az storage container list --account-name {{스토리지_계정_이름}} --prefix {{필터_접두사}}`

- 지정된 컨테이너를 삭제하도록 표시:

`az storage container delete --account-name {{스토리지_계정_이름}} --name {{컨테이너_이름}} --fail-not-exist`
