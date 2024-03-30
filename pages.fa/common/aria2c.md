# aria2c

> ابزاری برای دانلود سریع.
> قابلیت پشتیبانی از Http(s), FTP, SFTP, BitTorrent, Metalink.
> اطلاعات بیشتر: <https://aria2.github.io>.

- دانلود لینک موردنظر و ذخیره در فایل:

`aria2c "{{url}}"`

- دانلود یک فایل از لینک موردنظر با اسم خروجی دلخواه:

`aria2c --out={{path/to/file}} "{{url}}"`

- دانلود چند فایل مختلف به صورت همزمان:

`aria2c --force-sequential {{false}} "{{url1 url2 ...}}"`

- دانلود از چند لینک مختلف:

`aria2c "{{url1 url2 ...}}"`

- دانلود لینک های لیست شده در یک فایل همراه با تنظیم تعداد دانلود های همزمان:

`aria2c --input-file={{path/to/file}} --max-concurrent-downloads={{number_of_downloads}}`

- دانلود با چندین اتصال مختلف:

`aria2c --split={{number_of_connections}} "{{url}}"`

- دانلود از FTP با نام کاربری و رمزعبور:

`aria2c --ftp-user={{username}} --ftp-passwd={{password}} "{{url}}"`

- محدود کردن سرعت دانلود با واحد بایت بر ثانیه:

`aria2c --max-download-limit={{speed}} "{{url}}"`
