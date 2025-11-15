# aws iam

> AWS 서비스에 대한 접근을 안전하게 제어하기 위한 웹 서비스인 IAM(Identity and Access Management)과 상호작용.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- 사용자 나열:

`aws iam list-users`

- 정책 나열:

`aws iam list-policies`

- 그룹 나열:

`aws iam list-groups`

- 그룹 내 사용자 가져오기:

`aws iam get-group --group-name {{그룹_이름}}`

- IAM 정책 표시:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{정책_이름}}`

- 액세스 키 나열:

`aws iam list-access-keys`

- 특정 사용자의 액세스 키 나열:

`aws iam list-access-keys --user-name {{사용자_이름}}`

- 도움말 표시:

`aws iam help`
