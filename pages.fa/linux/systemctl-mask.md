# systemctl mask

> پیوند دادن واحدها به `/dev/null` تا نتوان آن‌ها را شروع کرد.
> همچنین : `systemctl revert`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#mask%20UNIT%E2%80%A6>.

- ماسک کردن سرویس:

`systemctl mask {{service_name}}`

- اطمینان از خاموش شدن سرویس هنگام ماسک کردن:

`systemctl mask {{service_name}} --now`

- ماسک کردن سرویس کاربر:

`systemctl mask {{service_name}} --user`
