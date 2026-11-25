# ndctl

> ابزار مدیریت DIMMهای حافظهٔ پایدار.
> اطلاعات بیشتر: <https://manned.org/ndctl>.

- ایجاد فضای نام در حالت `fsdax`:

`ndctl create-namespace --mode={{fsdax}}`

- تغییر حالت فضای نام به `raw`:

`ndctl create-namespace --reconfigure={{namespaceX.Y}} --mode={{raw}}`

- بررسی سازگاری فضای نام حالت sector و تعمیر در صورت نیاز:

`ndctl check-namespace --repair {{namespaceX.Y}}`

- فهرست کردن همهٔ فضاهای نام، ناحیه‌ها و گذرگاه‌ها (از جمله موارد غیرفعال):

`ndctl list --namespaces --regions --buses --idle`

- فهرست کردن فضای نام مشخص همراه با اطلاعات اضافی فراوان:

`ndctl list -vvv --namespace={{namespaceX.Y}}`

- اجرای پایشگر برای نظارت بر رویدادهای سلامت SMART مربوط به NVDIMMها در گذرگاه `ACPI.NFIT`:

`ndctl monitor --bus={{ACPI.NFIT}}`

- حذف فضای نام (در صورت امکان) یا بازنشانی آن به وضعیت اولیه:

`ndctl destroy-namespace --force {{namespaceX.Y}}`
