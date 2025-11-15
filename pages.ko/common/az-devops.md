# az devops

> Azure DevOps 조직을 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/devops>.

- 특정 조직에 로그인하려면 개인 액세스 토큰(PAT)을 설정:

`az devops login --organization {{조직_url}}`

- 브라우저에서 프로젝트를 열기:

`az devops project show --project {{프로젝트_이름}} --open`

- 특정 프로젝트에 참여하는 특정 팀의 구성원을 나열:

`az devops team list-member --project {{프로젝트_이름}} --team {{팀_이름}}`

- Azure DevOps CLI 현재 구성을 확인:

`az devops configure --list`

- 기본 프로젝트와 기본 조직을 설정하여 Azure DevOps CLI 동작을 구성:

`az devops configure --defaults project={{프로젝트_이름}} organization={{조직_url}}`
