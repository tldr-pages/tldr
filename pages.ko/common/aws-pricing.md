# aws pricing

> Amazon Web Services에서 서비스, 제품 및 가격 정보를 쿼리.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/pricing/>.

- 특정 지역의 서비스 코드 나열:

`aws pricing describe-services --region {{us-east-1}}`

- 특정 지역의 지정된 서비스 코드에 대한 속성을 나열:

`aws pricing describe-services --service-code {{AmazonEC2}} --region {{us-east-1}}`

- 특정 지역의 서비스 코드에 대한 가격 정보 출력:

`aws pricing get-products --service-code {{AmazonEC2}} --region {{us-east-1}}`

- 특정 지역의 서비스 코드에 대한 특정 속성 값 나열:

`aws pricing get-attribute-values --service-code {{AmazonEC2}} --attribute-name {{인스턴스타입}} --region {{us-east-1}}`

- 인스턴스 유형 및 위치에 대한 필터를 사용하여, 서비스 코드에 대한 가격 정보를 출력:

`aws pricing get-products --service-code {{AmazonEC2}} --filters "{{Type=TERM_MATCH,Field=instanceType,Value=m5.xlarge}}" "{{Type=TERM_MATCH,Field=location,Value=US East (N. Virginia)}}" --region {{us-east-1}}`
