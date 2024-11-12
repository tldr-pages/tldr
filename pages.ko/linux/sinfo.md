# sinfo

> Slurm 노드 및 파티션 정보를 표시합니다.
> 같이 보기: `squeue` 및 `sbatch`, 이는 Slurm 작업 관리자에 포함됩니다.
> 더 많은 정보: <https://slurm.schedmd.com/sinfo.html>.

- 클러스터의 빠른 요약 개요 표시:

`sinfo --summarize`

- 클러스터 전체의 모든 파티션에 대한 자세한 상태 보기:

`sinfo`

- 특정 파티션에 대한 자세한 상태 보기:

`sinfo --partition {{파티션_이름}}`

- 유휴 노드 정보 보기:

`sinfo --states {{idle}}`

- 죽은 노드 요약:

`sinfo --dead`

- 죽은 노드와 그 이유 나열:

`sinfo --list-reasons`
