# sbatch

> ارسال کار دسته‌ای به زمان‌بند SLURM.
> اطلاعات بیشتر: <https://manned.org/sbatch>.

- ارسال کار دسته‌ای:

`sbatch {{path/to/job.sh}}`

- ارسال کار دسته‌ای با نام دلخواه:

`sbatch --job-name={{myjob}} {{path/to/job.sh}}`

- ارسال کار دسته‌ای با محدودیت زمانی ۳۰ دقیقه:

`sbatch --time={{00:30:00}} {{path/to/job.sh}}`

- ارسال کار و درخواست چند گره:

`sbatch --nodes={{3}} {{path/to/job.sh}}`
