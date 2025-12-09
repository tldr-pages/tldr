# aws ecr

> 컨테이너 이미지 추가, 당겨오기 및 관리.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html>.

- 기본 레지스트리로 Docker 인증 (사용자 이름은 AWS):

`aws ecr get-login-password --region {{리전}} | {{docker login}} --username AWS --password-stdin {{aws_계정_아이디}}.dkr.ecr.{{리전}}.amazonaws.com`

- 저장소 생성:

`aws ecr create-repository --repository-name {{저장소}} --image-scanning-configuration scanOnPush={{true|false}} --region {{리전}}`

- ECR용 로컬 이미지에 태그 지정:

`docker tag {{컨테이너_이름}}:{{태그}} {{aws_계정_아이디}}.dkr.ecr.{{리전}}.amazonaws.com/{{컨테이너_이름}}:{{태그}}`

- 저장소에 이미지 추가:

`docker push {{aws_계정_아이디}}.dkr.ecr.{{리전}}.amazonaws.com/{{컨테이너_이름}}:{{태그}}`

- 저장소에서 이미지 가져오기:

`docker pull {{aws_계정_아이디}}.dkr.ecr.{{리전}}.amazonaws.com/{{컨테이너_이름}}:{{태그}}`

- 저장소에서 이미지 삭제:

`aws ecr batch-delete-image --repository-name {{저장소}} --image-ids imageTag={{latest}}`

- 저장소 삭제:

`aws ecr delete-repository --repository-name {{저장소}} --force`

- 저장소 안 이미지 나열:

`aws ecr list-images --repository-name {{저장소}}`
