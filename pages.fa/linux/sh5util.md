# sh5util

> ادغام فایل‌های HDF5 تولیدشده توسط افزونهٔ `sacct_gather_profile`.
> اطلاعات بیشتر: <https://slurm.schedmd.com/sh5util.html>.

- ادغام فایل‌های HDF5 تولیدشده در هر گرهٔ تخصیص‌یافته برای کار یا مرحلهٔ مشخص:

`sh5util {{[-j|--jobs]}} {{job_id|job_id.step_id}}`

- استخراج یک یا چند سری داده از فایل کار ادغام‌شده:

`sh5util {{[-j|--jobs]}} {{job_id|job_id.step_id}} {{[-E|--extract]}} {{[-i|--input]}} {{path/to/file.h5}} {{[-s|--series]}} {{Energy|Filesystem|Network|Task}}`

- استخراج یک داده از همهٔ گره‌ها در فایل کار ادغام‌شده:

`sh5util {{[-j|--jobs]}} {{job_id|job_id.step_id}} {{[-I|--item-extract]}} {{[-s|--series]}} {{Energy|Filesystem|Network|Task}} {{[-d|--data]}} {{data_item}}`
