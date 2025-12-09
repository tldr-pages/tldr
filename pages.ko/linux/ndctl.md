# ndctl

> 비휘발성 DIMM을 관리하는 도구.
> 더 많은 정보: <https://manned.org/ndctl>.

- 'fsdax' 모드 네임스페이스 생성:

`ndctl create-namespace --mode={{fsdax}}`

- 네임스페이스 모드를 'raw'로 변경:

`ndctl create-namespace --reconfigure={{namespaceX.Y}} --mode={{raw}}`

- 섹터 모드 네임스페이스의 일관성을 검사하고 필요 시 복구:

`ndctl check-namespace --repair {{namespaceX.Y}}`

- 모든 네임스페이스, 영역, 버스 나열 (비활성 포함):

`ndctl list --namespaces --regions --buses --idle`

- 특정 네임스페이스를 나열하고 추가 정보를 많이 포함:

`ndctl list -vvv --namespace={{namespaceX.Y}}`

- 'ACPI.NFIT' 버스에서 NVDIMM의 SMART 상태 이벤트 모니터링 실행:

`ndctl monitor --bus={{ACPI.NFIT}}`

- 네임스페이스 제거 (적용 가능한 경우) 또는 초기 상태로 재설정:

`ndctl destroy-namespace --force {{namespaceX.Y}}`
