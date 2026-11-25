# b4 am

> دریافت و آماده‌سازی وصله‌ها از یک بایگانی public-inbox برای اعمال با `git am`.
> اطلاعات بیشتر: <https://b4.docs.kernel.org/en/latest/maintainer/am-shazam.html>.

- دریافت وصله‌ها از یک رشتهٔ پیام و آماده‌سازی آن‌ها برای `git am`:

`b4 am {{message_id}}`

- دریافت وصله‌ها و افزودن پانوشت‌های `Signed-off-by` خودتان و `Link:` به هر کامیت:

`b4 am {{[-sl|--add-my-sob --add-link]}} {{message_id}}`

- دریافت وصله‌ها و آماده‌سازی با پشتیبانی از ادغام سه‌طرفه برای رفع تعارض:

`b4 am {{[-3|--prep-3way]}} {{message_id}}`

- انتخاب و اعمال زیرمجموعه‌ای از وصله‌های یک مجموعه (برای مثال، وصله‌های ۱ تا ۳ و ۵):

`b4 am {{[-P|--cherry-pick]}} {{1-3,5}} {{message_id}}`

- دریافت وصله‌ها و اجرای بررسی‌های محلی روی هر وصله:

`b4 am --check {{message_id}}`

- ذخیرهٔ صندوق پستی خروجی در یک دایرکتوری مشخص:

`b4 am {{[-o|--outdir]}} {{path/to/directory}} {{message_id}}`
