# cage

> باز کردن برنامه‌ها در حالت کیوسک.
> همچنین ببینید: `gamescope`.
> اطلاعات بیشتر: <https://github.com/cage-kiosk/cage/blob/master/cage.1.scd>.

- اجرای یک برنامه:

`cage {{application}}`

- دادن آرگومان به برنامه:

`cage -- {{application}} {{arguments}}`

- پنهان کردن تزئینات پنجره با `-d` (ممکن است دسترسی شما به پایانه را مسدود کند):

`cage -d {{application}}`

- اجازه دادن به جابه‌جایی پایانه‌ها با `<Ctrl Alt F2>` با استفاده از `-s`:

`cage -s {{application}}`

- اجرای یک فایل مشخص:

`cage /{{path/to/file}}`

- نمایش راهنما:

`cage -h`
