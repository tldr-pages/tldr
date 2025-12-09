# az repos

> Azure DevOps 레포지토리를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/repos>.

- 특정 프로젝트의 모든 저장소 나열:

`az repos list --project {{프로젝트_이름}}`

- 특정 저장소의 특정 분기에 정책을 추가해, 기본 병합을 제한:

`az repos policy merge-strategy create --repository-id {{저장소_목록_내부_레포지토리}} --branch {{브랜치_이름}} --blocking --enabled --allow-no-fast-forward false --allow-rebase true --allow-rebase-merge true --allow-squash true`

- 소스 업데이트 할때 자동으로 추적되도록 기존 빌드 파이프라인을 사용하여, 특정 저장소에 빌드 유효성 검사를 추가:

`az repos policy build create --repository-id {{레포지토리_아이디}} --build-definition-id {{빌드_파이프라인_아이디}} --branch main --blocking --enabled --queue-on-source-update-only true --display-name {{이름}} --valid-duration {{분}}`

- 특정 프로젝트 내의 특정 저장소의 모든 활성 끌어오기 요청을 나열:

`az repos pr list --project {{프로젝트_이름}} --repository {{레포지토리_이름}} --status active`
