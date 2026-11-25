# sleep

> تأخیر به مدت مشخص.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/sleep-invocation.html>.

- تأخیر بر حسب ثانیه:

`sleep {{seconds}}`

- تأخیر بر حسب دقیقه (واحدهای روز، ساعت، ثانیه و بی‌نهایت نیز قابل استفاده‌اند):

`sleep {{minutes}}m`

- تأخیر به مدت ۱ روز و ۳ ساعت:

`sleep 1d 3h`

- اجرای دستور مشخص پس از ۲۰ دقیقه تأخیر:

`sleep 20m && {{command}}`

- تأخیر بی‌پایان:

`sleep {{[inf|infinity]}}`

- تأخیر به مدت یک میلی‌ثانیه:

`sleep {{0.001|1e-3}}`

- نمایش راهنما:

`sleep --help`
