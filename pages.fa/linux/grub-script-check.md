# grub-script-check

> برنامهٔ `grub-script-check` فایل اسکریپت GRUB را دریافت و از نظر خطاهای نحوی بررسی می‌کند.
> می‌تواند مسیر را به‌عنوان آرگومان غیرگزینه‌ای بگیرد؛ در صورت ارائه نشدن از ورودی استاندارد `stdin` می‌خواند.
> اطلاعات بیشتر: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dscript_002dcheck>.

- بررسی فایل اسکریپت مشخص برای خطاهای نحوی:

`grub-script-check {{path/to/grub_config_file}}`

- نمایش هر خط ورودی پس از خواندن آن:

`grub-script-check {{[-v|--verbose]}}`

- نمایش راهنما:

`grub-script-check --help`

- نمایش نسخه:

`grub-script-check --version`
