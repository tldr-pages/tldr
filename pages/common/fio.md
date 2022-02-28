# fio

> flexible I/O tester 
> Tool that will spawn a number of threads or processes doing a particular type of I/O action
> More examples: <https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm>.

- Test random reads

`fio --filename=device name --direct=1 --rw=randread --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=iops-test-job --eta-newline=1 --readonly`

- Test sequential reads

`sudo fio --filename=device name --direct=1 --rw=read --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=iops-test-job --eta-newline=1 --readonly`

- Test random read/write

`sudo fio --filename=/custom mount point/file --size=500GB --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=iops-test-job --eta-newline=1`

