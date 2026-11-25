# b4 send

> ارسال یک مجموعهٔ وصلهٔ آماده‌شده با `b4 prep` به فهرست رایانامه.
> اطلاعات بیشتر: <https://b4.docs.kernel.org/en/latest/contributor/send.html>.

- ارسال وصله‌ها از شاخهٔ فعلی تحت پیگیری prep:

`b4 send`

- تولید پیام‌ها برای بازبینی بدون ارسال آن‌ها:

`b4 send {{[-o|--output-dir]}} {{path/to/directory}}`

- ارسال وصله‌ها به گیرندگان مشخص برای پیش‌نمایش بدون افزایش نسخهٔ مجموعه:

`b4 send --preview-to {{email_address1 email_address2 ...}}`

- ارسال مجدد نسخه‌ای از مجموعه که قبلاً ارسال شده است:

`b4 send --resend {{version_number}}`

- شبیه‌سازی ارسال مجموعهٔ وصله‌ها بدون ارسال رایانامه:

`b4 send {{[-d|--dry-run]}}`
