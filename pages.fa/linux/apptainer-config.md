# apptainer config

> مدیریت پیکربندی‌های مختلف Apptainer.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_config.html>.

- افزودن یک نگاشت کاربر fakeroot:

`sudo apptainer config fakeroot {{[-a|--add]}} {{username}}`

- حذف یک نگاشت کاربر fakeroot:

`sudo apptainer config fakeroot {{[-r|--remove]}} {{username}}`

- فعال کردن یک نگاشت کاربر fakeroot:

`sudo apptainer config fakeroot {{[-e|--enable]}} {{username}}`

- غیرفعال کردن یک نگاشت کاربر fakeroot:

`sudo apptainer config fakeroot {{[-d|--disable]}} {{username}}`

- دریافت مقدار فعلی یک دستورالعمل پیکربندی سراسری:

`sudo apptainer config global {{[-g|--get]}} {{directive}}`

- تنظیم مقدار یک دستورالعمل پیکربندی سراسری:

`sudo apptainer config global {{[-s|--set]}} {{directive}} {{value}}`

- حذف مقدار تنظیم‌شده برای یک دستورالعمل پیکربندی سراسری:

`sudo apptainer config global {{[-u|--unset]}} {{directive}} {{value}}`

- بازگرداندن یک دستورالعمل پیکربندی سراسری به مقدار پیش‌فرض:

`sudo apptainer config global {{[-r|--reset]}} {{directive}}`
