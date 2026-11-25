# btrfs send

> انتقال داده‌ها (زیرحجم یا عکس لحظه‌ای) از یک سیستم فایل به دیگری در قالبی قابل ارسال به‌صورت جریان.
> توجه: `send` نیاز دارد عکس لحظه‌ای فقط‌خواندنی باشد.
> همچنین ببینید: `btrfs-subvolume`, `btrfs-property`.
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/Send-receive.html>.

- ارسال عکس لحظه‌ای یک زیرحجم به فایل به جای خروجی استاندارد `stdout`:

`sudo btrfs send -f {{path/to/file.btrfs}} {{path/to/source_snapshot}}`

- بازیابی عکس لحظه‌ای یک زیرحجم از فایل به جای ورودی استاندارد `stdin`:

`sudo btrfs receive -f {{path/to/file.btrfs}} {{path/to/destination_directory}}`

- ارسال جریان عکس لحظه‌ای یک زیرحجم و انتقال آن با لوله به مقصد دریافت‌کننده:

`sudo btrfs send {{path/to/source_snapshot}} | sudo btrfs receive {{path/to/destination_directory}}`

- ارسال یک به‌روزرسانی افزایشی (تفاوت‌های بین عکس لحظه‌ای والد و جدید) به فایل:

`sudo btrfs send -p {{path/to/parent_snapshot}} -f {{path/to/incremental.btrfs}} {{path/to/new_snapshot}}`

- ارسال جریان یک به‌روزرسانی افزایشی و انتقال آن با لوله به مقصد دریافت‌کننده:

`sudo btrfs send -p {{path/to/parent_snapshot}} {{path/to/new_snapshot}} | sudo btrfs receive {{path/to/destination_directory}}`

- ارسال عکس لحظه‌ای یک زیرحجم از طریق SSH (باید `sudo` در سمت دریافت‌کننده برای اجرا بدون رمز عبور پیکربندی شده باشد):

`sudo btrfs send {{path/to/source_snapshot}} | ssh {{user}}@{{host}} "sudo btrfs receive {{path/to/destination_directory}}"`

- چاپ فرادادهٔ جریان از یک فایل بدون تغییر سیستم فایل:

`sudo btrfs receive --dump -f {{path/to/file.btrfs}}`
