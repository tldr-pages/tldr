# fio

> 灵活的I/O测试工具：通过生成多个线程或进程来执行I/O操作。
> 更多信息：<https://fio.readthedocs.io/en/latest/fio_doc.html>.

- 测试随机读取：

`fio --filename={{path/to/file}} --direct=1 --rw=randread --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1 --readonly`

- 测试顺序读取：

`fio --filename={{path/to/file}} --direct=1 --rw=read --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1 --readonly`

- 测试随机读写：

`fio --filename={{path/to/file}} --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1`

- 使用任务文件中的参数进行测试：

`fio {{path/to/job_file}}`

- 将特定任务文件转换为命令行选项：

`fio --showcmd {{path/to/job_file}}`