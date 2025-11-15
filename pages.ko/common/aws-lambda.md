# aws lambda

> 서버를 프로비저닝하거나 관리하지 않고도 코드를 실행하기 위한 컴퓨팅 서비스인 AWS Lambda를 사용.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- 함수 실행:

`aws lambda invoke --function-name {{이름}} {{경로/대상/응답.json}}`

- JSON 형식의 입력 페이로드를 사용하여 함수를 실행:

`aws lambda invoke --function-name {{이름}} --payload {{json}} {{경로/대상/응답.json}}`

- 함수 나열:

`aws lambda list-functions`

- 함수 구성 설정을 표시:

`aws lambda get-function-configuration --function-name {{이름}}`

- 함수 별칭 나열:

`aws lambda list-aliases --function-name {{이름}}`

- 함수에 대해 예약된 동시성 구성 설정을 표시:

`aws lambda get-function-concurrency --function-name {{이름}}`

- 함수를 호출할 수 있는 AWS 서비스를 나열:

`aws lambda get-policy --function-name {{이름}}`
