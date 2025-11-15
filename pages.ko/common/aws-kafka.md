# aws kafka

> Amazon MSK (Apache Kafka용 관리형 스트리밍) 클러스터 관리.
> 추가 정보: `aws`.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/kafka/index.html>.

- 새로운 MSK 클러스터 만들기:

`aws kafka create-cluster --cluster-name {{클러스터_이름}} --broker-node-group-info instanceType={{인스턴스_타입}},clientSubnets={{서브넷_아이디1 서브넷_아이디2 ...}} --kafka-version {{버전}} --number-of-broker-nodes {{숫자}}`

- MSK 클러스터 정보 표시:

`aws kafka describe-cluster --cluster-arn {{cluster_arn}}`

- 현재 지역의 모든 MSK 클러스터 목록 나열:

`aws kafka list-clusters`

- 새로운 MSK 구성 파일 생성:

`aws kafka create-configuration --name {{구성파일_이름}} --server-properties file://{{경로/대상/구성파일_이름.txt}}`

- MSK 구성파일 내용 표시:

`aws kafka describe-configuration --arn {{configuration_arn}}`

- 현재 지역의 모든 MSK 구성 나열:

`aws kafka list-configurations`

- MSK 클러스터 구성 업데이트:

`aws kafka update-cluster-configuration --cluster-arn {{cluster_arn}} --configuration-info arn={{configuration_arn}},revision={{configuration_revision}}`

- MSK 클러스터 삭제:

`aws kafka delete-cluster --cluster-arn {{cluster_arn}}`
