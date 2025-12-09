# az pipelines

> Azure Pipelines 리소스를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/pipelines>.

- 새로운 Azure 파이프라인(YAML 기반)을 생성:

`az pipelines create --org {{조직_url}} --project {{프로젝트_이름}} --name {{파이프라인_이름}} --description {{구독}} --repository {{레포지토리_이름}} --branch {{브랜치_이름}}`

- 특정 파이프라인 삭제:

`az pipelines delete --org {{조직_url}} --project {{프로젝트_이름}} --id {{파이프라인_아이디}}`

- 파이프라인 나열:

`az pipelines list --org {{조직_url}} --project {{프로젝트_이름}}`

- 실행할 특정 파이프라인을 대기열에 추가:

`az pipelines run --org {{organization_url}} --project {{프로젝트_이름}} --name {{파이프라인_이름}}`

- 특정 파이프라인의 세부정보를 가져옴:

`az pipelines show --org {{조직_url}} --project {{프로젝트_이름}} --name {{파이프라인_이름}}`

- 특정 파이프라인 업데이트:

`az pipelines update --org {{조직_url}} --project {{프로젝트_이름}} --name {{파이프라인_이름}} --new-name {{새로운_파이프라인_이름}} --new-folder-path {{user1/production_pipelines}}`

- 풀의 모든 에이전트를 나열:

`az pipelines agent list --org {{조직_url}} --pool-id {{agent_pool}}`
