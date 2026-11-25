# rfkill

> فعال و غیرفعال کردن دستگاه‌های بی‌سیم.
> اطلاعات بیشتر: <https://manned.org/rfkill>.

- فهرست کردن دستگاه‌ها:

`rfkill`

- فیلتر بر اساس ستون‌ها:

`rfkill {{[-o|--output]}} {{ID,TYPE,DEVICE,...}}`

- مسدود کردن دستگاه‌ها بر اساس نوع:

`rfkill block {{bluetooth|wifi|gps|nfc|...}}`

- رفع مسدودیت دستگاه‌ها بر اساس نوع:

`rfkill unblock {{bluetooth|wifi|gps|nfc|...}}`

- خروجی در قالب JSON:

`rfkill {{[-J|--json]}}`
