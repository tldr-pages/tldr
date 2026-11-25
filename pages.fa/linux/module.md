# module

> تغییر محیط کاربران.
> اطلاعات بیشتر: <https://lmod.readthedocs.io/en/latest/010_user.html>.

- نمایش ماژول‌های موجود:

`module avail`

- جست‌وجوی ماژول با نام:

`module avail {{module_name}}`

- بارگذاری ماژول:

`module load {{module_name}}`

- نمایش ماژول‌های بارگذاری‌شده:

`module list`

- خارج کردن ماژول مشخص از حافظه:

`module unload {{module_name}}`

- خارج کردن همهٔ ماژول‌های بارگذاری‌شده از حافظه:

`module purge`

- تعیین ماژول‌های ساخته‌شده توسط کاربر:

`module use {{path/to/module_file1 path/to/module_file2 ...}}`

- ذخیرهٔ مجموعهٔ فعلی ماژول‌های بارگذاری‌شده:

`module save {{collection_name}}`
