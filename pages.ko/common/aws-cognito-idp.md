# aws cognito-idp

> Configure an Amazon Cognito user pool and its users and groups and authenticate them.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>.

- 새로운 Cognito 사용자 풀 생성:

`aws cognito-idp create-user-pool --pool-name {{이름}}`

- 모든 사용자 풀 나열 :

`aws cognito-idp list-user-pools --max-results {{10}}`

- 특정 사용자 풀 삭제:

`aws cognito-idp delete-user-pool --user-pool-id {{사용자_풀_아이디}}`

- 특정 풀에 사용자 생성:

`aws cognito-idp admin-create-user --username {{사용자명}} --user-pool-id {{사용자_풀_아이디}}`

- 특정 풀의 사용자 나열:

`aws cognito-idp list-users --user-pool-id {{사용자_풀_아이디}}`

- 특정 풀에서 사용자 삭제:

`aws cognito-idp admin-delete-user --username {{사용자명}} --user-pool-id {{사용자_풀_아이디}}`
