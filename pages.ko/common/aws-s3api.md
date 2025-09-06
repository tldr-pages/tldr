# aws s3api

> Amazon S3 버킷을 생성 및 삭제하고 버킷 속성을 편집.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html>.

- 특정 리전에 버킷 생성:

`aws s3api create-bucket --bucket {{버킷_이름}} --region {{리전}} --create-bucket-configuration LocationConstraint={{리전}}`

- 버킷 삭제:

`aws s3api delete-bucket --bucket {{버킷_이름}}`

- 버킷 나열:

`aws s3api list-buckets`

- 버킷 내부의 객체를 나열하고, 각 객체의 키와 크기만 표시:

`aws s3api list-objects --bucket {{버킷_이름}} --query '{{Contents[].{Key: Key, Size: Size}}}'`

- 버킷에 객체를 추가:

`aws s3api put-object --bucket {{버킷_이름}} --key {{object_key}} --body {{path/to/file}}`

- 버킷에서 객체 다운로드 (출력 파일은 항상 마지막 인수로 와야 함):

`aws s3api get-object --bucket {{버킷_이름}} --key {{객체_키}} {{경로/대상/출력_파일}}`

- 지정된 버킷에 Amazon S3 버킷 정책 적용:

`aws s3api put-bucket-policy --bucket {{버킷_이름}} --policy file://{{경로/대상/버킷_정책.json}}`

- 지정된 버킷에서 Amazon S3 버킷 정책 다운로드:

`aws s3api get-bucket-policy --bucket {{버킷_이름}} --query Policy --output {{json|table|text|yaml|yaml-stream}} > {{경로/대상/버킷_정책}}`
