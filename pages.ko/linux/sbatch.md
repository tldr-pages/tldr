# sbatch

> SLURM 스케줄러에 배치 작업 제출.
> 더 많은 정보: <https://manned.org/sbatch>.

- 배치 작업 제출:

`sbatch {{경로/대상/작업.sh}}`

- 사용자 지정 이름으로 배치 작업 제출:

`sbatch --job-name={{myjob}} {{경로/대상/작업.sh}}`

- 30분의 시간 제한으로 배치 작업 제출:

`sbatch --time={{00:30:00}} {{경로/대상/작업.sh}}`

- 여러 노드를 요청하여 작업 제출:

`sbatch --nodes={{3}} {{경로/대상/작업.sh}}`
