# aws s3 website

> 버킷의 웹사이트 구성 설정.
> 추가 정보: `aws s3`.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/s3/website.html>.

- 버킷을 정적 웹 사이트로 구성:

`aws s3 website {{s3://버킷-이름}} --index-document {{index.html}}`

- 웹 사이트에 대한 오류 페이지 구성:

`aws s3 website {{s3://버킷-이름}} --index-document {{index.html}} --error-document {{error.html}}`
