# systemd-inhibit

> جلوگیری از ورود سیستم به وضعیت‌های توان مشخص.
> قفل‌های ممانعت می‌توانند برای مسدود یا تأخیر کردن درخواست‌های خواب و خاموشی و مدیریت خودکار بی‌کاری استفاده شوند.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-inhibit.html>.

- فهرست کردن همهٔ قفل‌های ممانعت فعال و دلایل ایجاد آن‌ها:

`systemd-inhibit`

- مسدود کردن خاموشی سیستم برای تعداد ثانیهٔ مشخص با دستور `sleep`:

`systemd-inhibit --what shutdown sleep {{5}}`

- جلوگیری از خواب یا بی‌کاری سیستم تا پایان بارگیری:

`systemd-inhibit --what sleep:idle wget {{https://example.com/file}}`

- نادیده گرفتن بسته شدن درِ دستگاه تا خروج اسکریپت:

`systemd-inhibit --what sleep:handle-lid-switch {{path/to/script}}`

- نادیده گرفتن فشردن دکمهٔ برق هنگام اجرای دستور:

`systemd-inhibit --what handle-power-key {{command}}`

- شرح ایجادکننده و دلیل ایجاد ممانعت (پیش‌فرض: دستور و آرگومان‌های آن برای `--who` و `Unknown reason` برای `--why`):

`systemd-inhibit --who {{$USER}} --why {{reason}} --what {{operation}} {{command}}`
