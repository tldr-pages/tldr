# srun

> 대화형 슬럼 작업을 생성하거나 기존 작업에 연결합니다.
> 더 많은 정보: <https://slurm.schedmd.com/srun.html>.

- 기본 대화형 작업 제출:

`srun --pty /bin/bash`

- 다양한 속성으로 대화형 작업 제출:

`srun --ntasks-per-node={{코어_수}} --mem-per-cpu={{메모리_MB}} --pty /bin/bash`

- 작업이 실행 중인 워커 노드에 연결:

`srun --jobid={{작업_ID}} --pty /bin/bash`
