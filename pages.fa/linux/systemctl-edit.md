# systemctl edit

> ویرایش فایل‌های واحد systemd.
> همچنین ببینید: `systemctl revert`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#edit%20UNIT%E2%80%A6>.

- اعمال پوشش غیرویرانگر روی فایل واحد:

`sudo systemctl edit {{unit_file}}`

- ویرایش فایل واحد:

`sudo systemctl edit {{unit_file}} {{[-l|--full]}}`

- ایجاد فایل واحد جدید:

`sudo systemctl edit {{unit_file}} {{[-lf|--full --force]}}`

- اعمال پوشش روی فایل واحد کاربر:

`systemctl edit {{unit_file}} --user`
