# systemctl set-property

> تنظیم ویژگی‌های مشخص واحد در زمان اجرا.
> همچنین ببینید: `systemctl revert`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#set-property%20UNIT%20PROPERTY=VALUE%E2%80%A6>.

- تنظیم ویژگی برای سرویس در حال اجرا:

`systemctl set-property {{unit}} {{property}}={{value}}`

- تنظیم چند ویژگی هم‌زمان:

`systemctl set-property {{unit}} {{property_1=value_1 property_2=value_2 ...}}`

- تنظیم ویژگی فقط برای نشست زمان اجرای فعلی (غیرپایدار):

`systemctl set-property {{unit}} {{property}}={{value}} --runtime`

- بازنشانی ویژگی به مقدار پیش‌فرض:

`systemctl set-property {{unit}} {{property}}=`

- بازنشانی چند ویژگی به مقادیر پیش‌فرض:

`systemctl set-property {{unit}} {{property_1= property_2= ...}}`
