# sstat

> 실행 중인 작업에 대한 정보를 표시합니다.
> 더 많은 정보: <https://slurm.schedmd.com/sstat.html>.

- 쉼표로 구분된 작업 목록의 상태 정보를 표시:

`sstat --jobs={{작업_ID}}`

- 쉼표로 구분된 작업 목록의 작업 ID, 평균 CPU 및 평균 가상 메모리 크기를 파이프로 구분하여 표시:

`sstat --parsable --jobs={{작업_ID}} --format={{JobID,AveCPU,AveVMSize}}`

- 사용 가능한 필드 목록 표시:

`sstat --helpformat`
