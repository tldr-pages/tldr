# aws workmail

> Amazon WorkMail을 관리.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/index.html>.

- 모든 WorkMail 조직을 나열:

`aws workmail list-organizations`

- 특정 조직의 모든 사용자를 나열:

`aws workmail list-users --organization-id {{조직_아이디}}`

- 특정 조직에서 WorkMail 사용자를 생성:

`aws workmail create-user --name {{사용자명}} --display-name {{이름}} --password {{비밀번호}} --organization-id {{조직_아이디}}`

- 그룹/사용자를 WorkMail에 등록하고 활성화:

`aws workmail register-to-work-mail --entity-id {{엔티티_아이디}} --email {{이메일}} --organization-id {{조직_아이디}}`

- 특정 조직에 WorkMail 그룹을 생성:

`aws workmail create-group --name {{그룹_이름}} --organization-id {{조직_아이디}}`

- 특정 그룹에 구성원을 연결:

`aws workmail associate-member-to-group --group-id {{그룹_아이디}} --member-id {{멤버_아이디}} --organization-id {{조직_아이디}}`

- WorkMail에서 사용자/그룹 등록을 취소하고 비활성화:

`aws workmail deregister-from-work-mail --entity-id {{엔티티_아이디}} --organization-id {{조직_아이디}}`

- 조직에서 사용자 삭제:

`aws workmail delete-user --user-id {{사용자_아이디}} --organization-id {{조직_아이디}}`
