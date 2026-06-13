# exo iam

> Exoscale IAM 서비스를 관리.
> 더 많은 정보: <https://community.exoscale.com/product/iam/>.

- 모든 IAM 역할 목록 조회:

`exo iam role list`

- 새로운 API 키 생성:

`exo iam api-key create {{api_키_이름}} {{iam_역할_이름}}`

- 새로운 IAM 역할 생성:

`cat {{경로/대상/정책.json}} | exo iam role create {{iam_역할_이름}} --editable --policy -`

- 기존 IAM 역할의 정책 조회:

`exo iam role show {{iam_역할_이름}} --policy {{[-O|--output-format]}} {{json}} | jq .`

- 조직 기본 정책 업데이트 (기본 조직 정책은 조직 내 모든 API 키에 대해 적용됨):

`cat {{경로/대상/정책.json}} | exo iam org-policy update -`
