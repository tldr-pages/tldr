# sdiag

> `slurmctld` 실행에 대한 정보를 표시합니다.
> 더 많은 정보: <https://slurm.schedmd.com/sdiag.html>.

- `slurmctld` 실행과 관련된 모든 성능 카운터 표시:

`sdiag {{[-a|--all]}}`

- `slurmctld` 실행과 관련된 성능 카운터 재설정:

`sdiag {{[-r|--reset]}}`

- 출력 형식 지정:

`sdiag {{[-a|--all]}} --{{json|yaml}}`

- 명령을 보낼 클러스터 지정:

`sdiag {{[-a|--all]}} {{[-M|--cluster]}} {{클러스터_이름}}`
