# strigger

> Slurm 트리거 정보를 조회하거나 수정합니다.
> 트리거는 Slurm 클러스터에서 이벤트가 발생할 때 자동으로 실행되는 작업입니다.
> 더 많은 정보: <https://slurm.schedmd.com/strigger.html>.

- 새로운 트리거 등록: 지정된 이벤트가 발생할 때 지정된 프로그램을 실행:

`strigger --set --{{primary_database_failure|primary_slurmdbd_failure|primary_slurmctld_acct_buffer_full|primary_slurmctld_failure|...}} --program={{경로/대상/실행파일}}`

- 지정된 작업이 종료될 때 지정된 프로그램을 실행:

`strigger --set --jobid={{작업_ID}} --fini --program="{{경로/대상/실행파일}} {{인수1 인수2 ...}}"`

- 활성 트리거 보기:

`strigger --get`

- 지정된 작업과 관련된 활성 트리거 보기:

`strigger --get --jobid={{작업_ID}}`

- 지정된 트리거 삭제:

`strigger --clear {{트리거_ID}}`
