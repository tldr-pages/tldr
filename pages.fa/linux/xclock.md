# xclock

> نمایش زمان به‌صورت عقربه‌ای یا دیجیتال.
> اطلاعات بیشتر: <https://manned.org/xclock>.

- نمایش ساعت عقربه‌ای:

`xclock`

- نمایش ساعت دیجیتال ۲۴ ساعته فقط با ساعت و دقیقه:

`xclock -digital -brief`

- نمایش ساعت دیجیتال با رشتهٔ قالب strftime (ببینید strftime(3)):

`xclock -digital -strftime {{format}}`

- نمایش ساعت دیجیتال ۲۴ ساعته با ساعت، دقیقه و ثانیه که هر ثانیه به‌روز می‌شود:

`xclock -digital -strftime '%H:%M:%S' -update 1`

- نمایش ساعت دیجیتال ۱۲ ساعته فقط با ساعت و دقیقه:

`xclock -digital -twelve -brief`
