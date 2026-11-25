# modinfo

> استخراج اطلاعات ماژول هستهٔ لینوکس.
> همچنین ببینید: `kmod`.
> اطلاعات بیشتر: <https://manned.org/modinfo>.

- فهرست کردن همهٔ ویژگی‌های ماژول هسته:

`modinfo {{kernel_module}}`

- فهرست کردن فقط ویژگی مشخص:

`modinfo {{[-F|--field]}} {{author|description|license|parm|filename|version|...}} {{kernel_module}}`
