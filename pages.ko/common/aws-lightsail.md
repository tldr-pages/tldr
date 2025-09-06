# aws lightsail

> Amazon Lightsail 리소스 관리.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html>.

- 모든 가상 사설 서버 또는 인스턴스를 나열:

`aws lightsail get-instances`

- 모든 번들 나열 (인스턴스 플랜):

`aws lightsail list-bundles`

- 사용 가능한 모든 인스턴스 이미지 또는 청사진을 나열:

`aws lightsail list-blueprints`

- 인스턴스 생성:

`aws lightsail create-instances --instance-names {{이름}} --availability-zone {{리전}} --bundle-id {{nano_2_0}} --blueprint-id {{청사진_아이디}}`

- 특정 인스턴스의 상태를 출력:

`aws lightsail get-instance-state --instance-name {{이름}}`

- 특정 인스턴스 중지:

`aws lightsail stop-instance --instance-name {{이름}}`

- 특정 인스턴스 삭제:

`aws lightsail delete-instance --instance-name {{이름}}`
