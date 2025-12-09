# fio

> 유연한 I/O 테스터: 여러 스레드 또는 프로세스를 생성하는 I/O 작업을 수행.
> 더 많은 정보: <https://fio.readthedocs.io/en/latest/fio_doc.html>.

- 무작위 읽기 테스트:

`fio --filename={{경로/대상/파일}} --direct=1 --rw=randread --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1 --readonly`

- 순차 읽기 테스트:

`fio --filename={{경로/대상/파일}} --direct=1 --rw=read --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1 --readonly`

- 무작위 읽기/쓰기 테스트:

`fio --filename={{경로/대상/파일}} --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1`

- 작업 파일의 매개변수로 테스트:

`fio {{경로/대상/작업_파일}}`

- 특정 작업 파일을 명령줄 옵션으로 변환:

`fio --showcmd {{경로/대상/작업_파일}}`
