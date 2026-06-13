# az quantum

> Manage Azure Quantum 워크스페이스를 관리하고 양자 작업을 제출하는 명령어(프리뷰, quantum 확장이 필요).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/quantum>.

- 새로운 Azure Quantum 워크스페이스 생성:

`az quantum workspace create {{[-g|--resource-group]}} {{리소스_그룹}} {{[-l|--location]}} {{위치}} {{[-w|--workspace-name]}} {{워크스페이스}} {{[-a|--storage-account]}} {{내_스토리지_계정_이름}}`

- 모든 Azure Quantum 워크스페이스 목록 조회:

`az quantum workspace list`

- 기본 Azure Quantum 워크스페이스 설정:

`az quantum workspace set {{[-g|--resource-group]}} {{리소스_그룹}} {{[-w|--workspace-name]}} {{워크스페이스}}`

- 특정 타겟에 QIR 양자 작업 제출:

`az quantum job submit {{[-g|--resource-group]}} {{리소스_그룹}} {{[-w|--workspace-name]}} {{워크스페이스}} {{[-l|--location]}} {{위치}} {{[-t|--target-id]}} {{Id}} --job-name {{작업}} --job-input-file {{QirBitcode.bc}} --job-input-format {{qir.v1}}`

- Quantum 워크스페이스 내 모든 작업 목록 조회:

`az quantum job list {{[-g|--resource-group]}} {{리소스_그룹}} {{[-l|--location]}} {{위치}} {{[-w|--workspace-name]}} {{워크스페이스}}`

- 양자 작업 결과 출력:

`az quantum job output {{[-g|--resource-group]}} {{리소스_그룹}} {{[-w|--workspace-name]}} {{워크스페이스}} --job-id {{작업}}`

- 특정 지역에서 사용 가능한 제공자 목록 조회:

`az quantum offerings list {{[-l|--location]}} {{Location}}`

- 작업 제출을 위한 기본 타겟 설정:

`az quantum target set {{[-t|--target-id]}} {{아이디}}`
