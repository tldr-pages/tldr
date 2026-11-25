# scrontab

> مدیریت فایل‌های crontab مربوط به Slurm.
> اطلاعات بیشتر: <https://slurm.schedmd.com/scrontab.html>.

- نصب crontab جدید از فایل مشخص:

`scrontab {{path/to/file}}`

- ویرایش crontab کاربر فعلی:

`scrontab -e`

- ویرایش crontab کاربر مشخص:

`scrontab --user={{user_id}} -e`

- حذف crontab فعلی:

`scrontab -r`

- چاپ crontab کاربر فعلی در `stdout`:

`scrontab -l`
