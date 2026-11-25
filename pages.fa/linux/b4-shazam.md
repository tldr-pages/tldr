# b4 shazam

> دریافت و اعمال وصله‌ها از یک بایگانی public-inbox مستقیماً به درخت Git فعلی.
> اطلاعات بیشتر: <https://b4.docs.kernel.org/en/latest/maintainer/am-shazam.html>.

- دریافت وصله‌ها از یک رشتهٔ پیام و اعمال مستقیم آن‌ها به شاخهٔ فعلی:

`b4 shazam {{message_id}}`

- دریافت وصله‌ها و ایجاد یک `FETCH_HEAD` برای ادغام (مانند درخواست ادغام):

`b4 shazam {{[-H|--make-fetch-head]}} {{message_id}}`

- دریافت وصله‌ها و ادغام خودکار با استفاده از نامهٔ معرفی به‌عنوان پیام کامیت ادغام:

`b4 shazam {{[-M|--merge]}} {{message_id}}`

- دریافت وصله‌ها، افزودن پانوشت‌های `Signed-off-by` و `Link:` شما و سپس ادغام:

`b4 shazam {{[-slM|--add-my-sob --add-link --merge]}} {{message_id}}`

- دریافت وصله‌ها و شروع رفع تعارض تعاملی در صورت امکان:

`b4 shazam {{[-H|--make-fetch-head]}} --resolve {{message_id}}`
