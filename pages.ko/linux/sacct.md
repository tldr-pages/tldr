# sacct

> Slurm 서비스로부터 회계 데이터를 표시합니다.
> 더 많은 정보: <https://slurm.schedmd.com/sacct.html>.

- 최근 작업의 작업 ID, 작업 이름, 파티션, 계정, 할당된 CPU 수, 작업 상태 및 작업 종료 코드를 표시:

`sacct`

- 최근 작업의 작업 ID, 작업 상태 및 작업 종료 코드를 표시:

`sacct --brief`

- 작업의 할당을 표시:

`sacct --jobs {{작업_ID}} --allocations`

- 작업의 경과 시간, 작업 이름, 요청된 CPU 수 및 요청된 메모리를 표시:

`sacct --jobs {{작업_ID}} --format=Elapsed,JobName,ReqCPUS,ReqMem`

- 1주일 전부터 현재까지 발생한 최근 작업을 표시:

`sacct --starttime=$(date -d "1 week ago" +'%F')`

- 속성에 대해 더 많은 문자를 출력:

`sacct --format=JobID,JobName%100`
