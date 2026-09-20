# srun

> Slurm 워크로드 관리 시스템에서 명령을 실행.
> 더 많은 정보: <https://slurm.schedmd.com/srun.html>.

- 간단한 명령을 대화형으로 실행:

`srun hostname`

- 4개의 작업(CPU)으로 작업 실행:

`srun {{[-n|--ntasks]}} 4 {{경로/대상/프로그램}}`

- 8 GB 메모리를 할당하여 작업 실행:

`srun --mem 8G {{경로/대상/프로그램}}`

- 지정한 파티션에서 작업 실행:

`srun {{[-p|--partition]}} gpu {{경로/대상/프로그램}}`

- 작업을 실행하고 출력을 파일에 저장:

`srun {{경로/대상/프로그램}} > {{경로/대상/출력파일}}`
