# aws s3 rb

> 비어있는 S3 버킷 삭제.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/s3/rb.html>.

- 비어있는 S3 버킷 삭제:

`aws s3 rb s3://{{버킷_이름}}`

- S3 버킷 및 버전이 지정되지 않은 객체를 강제 삭제 (버전이 명시된 객체가 있는 경우 충돌 발생):

`aws s3 rb s3://{{버킷_이름}} --force`
