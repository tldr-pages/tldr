# bsub

> LSF (Load Sharing Facility) 스케줄러에 배치 작업을 제출하는 명령어.
> 더 많은 정보: <https://www.ibm.com/docs/spectrum-lsf/latest?topic=reference-bsub>.

- 스크립트 파일을 작업으로 제출:

`bsub {{경로/대상/스크립트.sh}}`

- 특정 큐에 작업 제출:

`bsub -q {{큐_이름}} make all`

- 작업이름 지정 및 출력/에러 로그 파일 설정:

`bsub -J {{작업_이름}} --output {{path/to/output.log}} --error {{path/to/error.log}} {{경로/대상/스크립트.sh}}`

- CPU 8코어와 메모리 16GB 요청하여 명령 실행:

`bsub -n 8 -M 16G cargo build --release`

- 현재 세션에서 대화형 쉘 실행:

`bsub -I bash`

- 실행 시간 제한(45분)을 설정하여 작업 제출:

`bsub -W 45 {{경로/대상/스크립트.sh}}`
