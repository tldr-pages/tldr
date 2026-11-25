# hlint

> پیشنهاد بهبود برای کد Haskell.
> اطلاعات بیشتر: <https://hackage.haskell.org/package/hlint>.

- نمایش پیشنهادها برای فایل مشخص:

`hlint {{path/to/file}} options`

- بررسی همهٔ فایل‌های Haskell و تولید گزارش:

`hlint {{path/to/directory}} {{[-r|--report]}}`

- اعمال خودکار بیشتر پیشنهادها:

`hlint {{path/to/file}} --refactor`

- نمایش گزینه‌های اضافی:

`hlint {{path/to/file}} --refactor-options`

- تولید فایل تنظیمات با نادیده گرفتن همهٔ پیشنهادهای موجود:

`hlint {{path/to/file}} --default >{{.hlint.yaml}}`
