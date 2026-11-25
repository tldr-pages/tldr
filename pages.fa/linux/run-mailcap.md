# run-mailcap

> اجرای برنامه‌ها از طریق مدخل‌های فایل mailcap.
> اطلاعات بیشتر: <https://manned.org/run-mailcap>.

- نوشتن فایل موجود یا جدید با ابزار ویرایش پیش‌فرض `mailcap`:

`run-mailcap --action=compose {{path/to/file}}`

- مشاهدهٔ فایل با نمایشگر پیش‌فرض `mailcap`:

`run-mailcap --action=edit {{path/to/file}}`

- چاپ فایل با ابزار چاپ پیش‌فرض `mailcap`:

`run-mailcap --action=print {{path/to/file}}`

- مشاهدهٔ فایل (معمولاً تصویر) با نمایشگر پیش‌فرض `mailcap`:

`run-mailcap --action=view {{path/to/file}}`

- فراخوانی اقدامات یا برنامه‌های منفرد در run-mailcap:

`run-mailcap --action={{view|cat|compose|composetyped|edit|print}} {{path/to/file}}`

- فعال کردن اطلاعات اضافی:

`run-mailcap --action={{action}} --debug {{path/to/file}}`

- نادیده گرفتن هر دستور «copiousoutput» و ارسال خروجی به `stdout`:

`run-mailcap --action={{action}} --nopager {{path/to/file}}`

- نمایش دستور یافت‌شده بدون اجرای واقعی آن:

`run-mailcap --action={{action}} --norun {{path/to/file}}`
