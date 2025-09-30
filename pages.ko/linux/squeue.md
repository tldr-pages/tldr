# squeue

> SLURM 스케줄러에 대기 중인 작업을 표시합니다.
> 더 많은 정보: <https://manned.org/squeue>.

- 대기열 보기:

`squeue`

- 특정 사용자에 의해 대기 중인 작업 보기:

`squeue -u {{사용자명}}`

- 대기열을 5초마다 새로고침하여 보기:

`squeue -i {{5}}`

- 예상 시작 시간과 함께 대기열 보기:

`squeue --start`
