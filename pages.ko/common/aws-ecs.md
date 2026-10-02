# aws ecs

> Elastic Container Service (ECS) 클러스터 관리.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/ecs/>.

- 태스크 정의 목록 표시:

`aws ecs list-task-definitions`

- 태스크 정의의 상세 표시:

`aws ecs describe-task-definition --task-definition {{태스크_정의}}`

- 태스크 정의를 생성하거나 새로운 리비전 등록:

`aws ecs register-task-definition --cli-input-json file://{{path_to_file.json}}`

- 태스크 정의를 등록 해제하여 INACTIVE 상태로 변경:

`aws ecs deregister-task-definition --task-definition {{태스크_정의}}:{{리비전_번호}}`

- 지정한 클러스터 서비스 목록 표시:

`aws ecs list-services --cluster {{클러스터_이름}}`

- 클러스터에 있는 하나 이상의 서비스 상세 정보 표시:

`aws ecs describe-services --services {{서비스_이름}} {{서비스_이름}} --cluster {{클러스터_이름}}`

- 서비스를 업데이트하고 새로운 배포를 강제 실행:

`aws ecs update-service --cluster {{클러스터_이름}} --service {{서비스_이름}} --task-definition {{태스크_정의_arn}} --force-new-deployment`

- 하나 이상의 서비스가 안정 상태가 될 때까지 대기:

`aws ecs wait services-stable --cluster {{클러스터_이름}} --services {{서비스_이름}} {{서비스_이름}}`
