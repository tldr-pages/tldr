# apptainer cache

> مدیریت حافظهٔ نهان محلی Apptainer.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_cache.html>.

- فهرست کردن همهٔ تصاویر کانتینر ذخیره‌شده در حافظهٔ نهان:

`apptainer cache list`

- فهرست کردن تصاویر کانتینر ذخیره‌شده در حافظهٔ نهان همراه با اطلاعات مفصل:

`apptainer cache list {{[-v|--verbose]}}`

- فهرست کردن فقط یک نوع مشخص از حافظهٔ نهان:

`apptainer cache list {{[-T|--type]}} {{library|oci|shub|blob|...}}`

- پاکسازی کل حافظهٔ نهان:

`apptainer cache clean`

- پاکسازی فقط یک نوع مشخص از حافظهٔ نهان:

`apptainer cache clean {{[-T|--type]}} {{library|oci|shub|blob|...}}`

- پاکسازی ورودی‌های حافظهٔ نهان قدیمی‌تر از تعداد روز مشخص:

`apptainer cache clean {{[-D|--days]}} {{days}}`

- شبیه‌سازی پاکسازی حافظهٔ نهان و نمایش مواردی که حذف خواهند شد:

`apptainer cache clean {{[-n|--dry-run]}}`

- پاکسازی اجباری بدون درخواست تأیید:

`apptainer cache clean {{[-f|--force]}}`
