# asterisk

> اجرا و مدیریت نمونه‌های سرور تلفن و مرکز تلفن.
> اطلاعات بیشتر: <https://docs.asterisk.org/Operation/>.

- اتصال مجدد به یک سرور در حال اجرا با `-r` و فعال کردن ثبت گزارش با سطح جزئیات ۳ با `-vvv`:

`asterisk -r -vvv`

- اتصال مجدد به یک سرور در حال اجرا با `-r`، اجرای یک دستور و بازگشت:

`asterisk -r -x "{{command}}"`

- نمایش کارخواه‌های chan_SIP (تلفن‌ها):

`asterisk -r -x "sip show peers"`

- نمایش تماس‌ها و کانال‌های فعال:

`asterisk -r -x "core show channels"`

- نمایش صندوق‌های پست صوتی:

`asterisk -r -x "voicemail show users"`

- خاتمه دادن به یک کانال:

`asterisk -r -x "hangup request {{channel_id}}"`

- بارگذاری مجدد پیکربندی chan_SIP:

`asterisk -r -x "sip reload"`
