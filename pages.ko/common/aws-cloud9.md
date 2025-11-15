# aws cloud9

> AWS Cloud9은 클라우드에서 소프트웨어를 작성, 빌드, 실행, 테스트, 디버그 및 릴리스하는 도구 모음입니다.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/index.html>.

- Cloud9 개발 환경 식별자 목록 가져오기:

`aws cloud9 list-environments`

- Cloud9 개발 환경 만들기:

`aws cloud9 create-environment-ec2 --name {{name}} --instance-type {{instance_type}}`

- Cloud9 개발 환경에 대한 정보 표시:

`aws cloud9 describe-environments --environment-ids {{environment_ids}}`

- Cloud9 개발 환경에 환경 멤버 추가:

`aws cloud9 create-environment-membership --environment-id {{environment_id}} --user-arn {{user_arn}} --permissions {{permissions}}`

- Cloud9 개발 환경에 대한 상태 정보 표시:

`aws cloud9 describe-environment-status --environment-id {{environment_id}}`

- Cloud9 환경 삭제:

`aws cloud9 delete-environment --environment-id {{environment_id}}`

- 개발 환경에서 환경 멤버 삭제:

`aws cloud9 delete-environment-membership --environment-id {{environment_id}} --user-arn {{user_arn}}`
