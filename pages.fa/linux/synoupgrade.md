# synoupgrade

> ارتقای Synology DiskStation Manager (DSM)، سیستم‌عامل NAS شرکت Synology.
> اطلاعات بیشتر: <https://www.synology.com/dsm>.

- بررسی وجود ارتقا:

`sudo synoupgrade --check`

- بررسی وصله‌ها بدون ارتقای نسخهٔ DSM:

`sudo synoupgrade --check-smallupdate`

- بارگیری جدیدترین ارتقای موجود (برای وصله‌ها از `--download-smallupdate` استفاده کنید):

`sudo synoupgrade --download`

- شروع فرایند ارتقا:

`sudo synoupgrade --start`

- ارتقای خودکار به جدیدترین نسخه:

`sudo synoupgrade --auto`

- اعمال خودکار وصله‌ها بدون ارتقای نسخهٔ DSM:

`sudo synoupgrade --auto-smallupdate`

- ارتقای DSM با فایل وصله (باید مسیر مطلق باشد):

`sudo synoupgrade --patch /{{path/to/file.pat}}`

- نمایش راهنما:

`synoupgrade`
