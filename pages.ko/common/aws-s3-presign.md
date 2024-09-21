# aws s3 presign

> Amazon S3 객체에 대해 미리 서명된 URL 생성.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html>.

- 한 시간 동안 유효한 특정 S3 객체에 대해 미리 서명된 URL을 생성:

`aws s3 presign s3://{{버킷_이름}}/{{경로/대상/파일}}`

- 특정 수명 동안 유효한 미리 서명된 URL을 생성:

`aws s3 presign s3://{{버킷_이름}}/{{경로/대상/파일}} --expires-in {{지속_시간}}`

- 도움말 표시:

`aws s3 presign help`
