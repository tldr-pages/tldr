# sreport

> 작업, 사용자, 클러스터에 대한 보고서를 회계 데이터에서 생성합니다.
> 더 많은 정보: <https://slurm.schedmd.com/sreport.html>.

- 파이프로 구분된 클러스터 사용량 데이터를 표시:

`sreport --parsable cluster utilization`

- 실행된 작업 수를 표시:

`sreport job sizes printjobcount`

- CPU 사용 시간이 가장 많은 사용자를 표시:

`sreport user topuser`
