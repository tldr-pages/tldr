# veracrypt

> نرم‌افزار رایگان و متن‌باز رمزگذاری دیسک.
> اطلاعات بیشتر: <https://arcanecode.com/2021/06/21/veracrypt-on-the-command-line-for-ubuntu-linux/>.

- ایجاد حجم جدید از طریق رابط متنی و استفاده از `/dev/urandom` به‌عنوان منبع دادهٔ تصادفی:

`veracrypt {{[-t|--text]}} {{[-c|--create]}} --random-source={{/dev/urandom}}`

- رمزگشایی تعاملی حجم از طریق رابط متنی و سوار کردن آن در دایرکتوری:

`veracrypt {{[-t|--text]}} {{path/to/volume}} {{path/to/mount_point}}`

- رمزگشایی پارتیشن با فایل کلید و سوار کردن آن در دایرکتوری:

`veracrypt {{[-k|--keyfiles]}} {{path/to/keyfile}} {{/dev/sdXN}} {{path/to/mount_point}}`

- پیاده کردن حجم از دایرکتوری محل اتصال آن:

`veracrypt {{[-d|--dismount]}} {{path/to/mounted_point}}`
