# srun

> ایجاد کار تعاملی slurm یا اتصال به کار موجود.
> اطلاعات بیشتر: <https://slurm.schedmd.com/srun.html>.

- ارسال کار تعاملی پایه:

`srun --pty /bin/bash`

- ارسال کار تعاملی با ویژگی‌های متفاوت:

`srun --ntasks-per-node {{num_cores}} --mem-per-cpu {{memory_MB}} --pty /bin/bash`

- اتصال به گره کاری دارای کار در حال اجرا:

`srun --jobid {{job_id}} --pty /bin/bash`
