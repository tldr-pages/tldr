# restic

> 빠르고 안전한 백업 프로그램.
> 더 많은 정보: <https://restic.readthedocs.io/en/stable/manual_rest.html#usage-help>.

- 지정된 로컬 디렉터리에 백업 저장소 초기화:

`restic init --repo {{경로/대상/저장소}}`

- 디렉터리를 저장소에 백업:

`restic --repo {{경로/대상/저장소}} backup {{경로/대상/폴더}}`

- 저장소에 현재 저장된 백업 스냅샷 표시:

`restic --repo {{경로/대상/저장소}} snapshots`

- 특정 백업 스냅샷을 대상 디렉터리에 복원:

`restic --repo {{경로/대상/저장소}} restore {{latest|스냅샷_ID}} --target {{경로/대상/타겟}}`

- 특정 백업의 특정 경로를 대상 디렉터리에 복원:

`restic --repo {{경로/대상/저장소}} restore {{스냅샷_ID}} --target {{경로/대상/타겟}} --include {{경로/대상/복원}}`

- 저장소를 정리하고 각 고유 백업의 최신 스냅샷만 유지:

`restic forget --keep-last 1 --prune`
