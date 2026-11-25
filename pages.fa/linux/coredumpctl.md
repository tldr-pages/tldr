# coredumpctl

> دریافت و پردازش core dumpها و فرادادهٔ ذخیره‌شده.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/coredumpctl.html>.

- فهرست کردن همهٔ core dumpهای ثبت‌شده:

`coredumpctl`

- فهرست کردن core dumpهای ثبت‌شده برای یک برنامه:

`coredumpctl list {{program_name}}`

- پالایش core dumpها بر اساس سیگنال مشخص:

`coredumpctl list COREDUMP_SIGNAL={{1..64}}`

- نمایش اطلاعات core dumpهای منطبق با برنامه‌ای با PID مشخص:

`coredumpctl info {{process_id}}`

- اجرای اشکال‌زدا با آخرین core dump:

`coredumpctl debug`

- اجرای اشکال‌زدا با آخرین core dump یک برنامه:

`coredumpctl debug {{program_name}}`

- استخراج آخرین core dump یک برنامه در فایل:

`coredumpctl dump {{program_name}} {{[-o|--output]}} {{path/to/file}}`

- صرف‌نظر از اعلان‌های debuginfod و صفحه‌بندی و سپس چاپ رد فراخوانی هنگام استفاده از `gdb`:

`coredumpctl debug {{[-A|--debugger-arguments]}} "-iex 'set debuginfod enabled on' -iex 'set pagination off' -ex bt"`
