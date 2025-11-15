# az storage blob

> Azure에서 blob 저장소 컨테이너 및 개체를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/storage/blob>.

- 소스([s]ource) 컨테이너를 지정하는 파일([f]ile) 경로에 blob를 다운로드:

`az storage blob download --account-name {{스토리지_계정_이름}} --account-key {{스토리지_계정_키}} -c {{컨테이너_이름}} -n {{경로/대상/blob}} -f {{경로/대상/로컬_파일}}`

- blob 컨테이너에서 blob을 재귀적으로 다운로드([d]ownload):

`az storage blob download-batch --account-name {{스토리지_계정_이름}} --account-key {{스토리지_계정_키}} -s {{컨테이너_이름}} -d {{경로/대상/remote}} --pattern {{파일이름_정규표현식}} --destination {{경로/대상/목적지}}`

- blob 스토리지에 로컬 파일을 업로드:

`az storage blob upload --account-name {{스토리지_계정_이름}} --account-key {{스토리지_계정_키}} -c {{컨테이너_이름}} -n {{경로/대상/blob}} -f {{경로/대상/로컬_파일}}`

- blob 객체 삭제:

`az storage blob delete --account-name {{스토리지_계정_이름}} --account-key {{스토리지_계정_키}} -c {{컨테이너_이름}} -n {{경로/대상/blob}}`

- blob에 대한 공유 액세스 서명을 생성:

`az storage blob generate-sas --account-name {{스토리지_계정_이름}} --account-key {{스토리지_계정_키}} -c {{컨테이너_이름}} -n {{경로/대상/blob}} --permissions {{permission_set}} --expiry {{Y-m-d'T'H:M'Z'}} --https-only`
