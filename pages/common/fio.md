# fio

> Flexible I/O tester.
> Tool that will spawn a number of threads or processes doing a particular type of I/O action.
> More information: <https://fio.readthedocs.io/en/latest/fio_doc.html>.

- Test random reads:

`sudo fio --filename={{path/to/file}} --direct=1 --rw=randread --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1 --readonly`

- Test sequential reads:

`sudo fio --filename={{path/to/file}} --direct=1 --rw=read --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1 --readonly`

- Test random read/write:

`sudo fio --filename={{path/to/file}} --size=500GB --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1`

- Test with parameters from a job file:

`sudo fio {{path/to/job_file}}`

- Convert a specific job file to command-line options:

`fio --showcmd {{path/to/job_file}}`
