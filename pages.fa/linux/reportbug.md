# reportbug

> ابزار گزارش اشکال توزیع Debian.
> اطلاعات بیشتر: <https://manned.org/reportbug>.

- تولید گزارش اشکال دربارهٔ بستهٔ مشخص و سپس ارسال آن با ایمیل:

`reportbug {{package}}`

- گزارش اشکالی که مربوط به بستهٔ مشخص نیست (مشکل عمومی، زیرساخت و غیره):

`reportbug other`

- نوشتن گزارش اشکال در فایل به‌جای ارسال با ایمیل:

`reportbug {{[-o|--output]}} {{filename}} {{package}}`
