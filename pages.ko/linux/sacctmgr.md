# sacctmgr

> Slurm 계정을 조회, 설정 및 관리.
> 더 많은 정보: <https://slurm.schedmd.com/sacctmgr.html>.

- 현재 구성 보기:

`sacctmgr show configuration`

- Slurm 데이터베이스에 클러스터 추가:

`sacctmgr add cluster {{클러스터_이름}}`

- Slurm 데이터베이스에 계정 추가:

`sacctmgr add account {{계정_이름}} cluster={{계정의_클러스터}}`

- 특정 형식을 사용하여 사용자/연관/클러스터/계정 세부 정보 보기:

`sacctmgr show {{user|association|cluster|account}} format="Account%10" format="GrpTRES%30"`
