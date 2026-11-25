# engrampa

> بسته‌بندی فایل‌ها در فایل `zip` یا `.tar` در محیط میزکار MATE.
> همچنین : `zip`, `tar`.
> اطلاعات بیشتر: <https://github.com/mate-desktop/engrampa>.

- شروع Engrampa:

`engrampa`

- باز کردن بایگانی‌های مشخص:

`engrampa {{path/to/archive1.tar path/to/archive2.tar ...}}`

- بایگانی بازگشتی فایل‌ها و یا دایرکتوری‌های مشخص:

`engrampa --add-to={{path/to/compressed.tar}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- استخراج فایل‌ها و یا دایرکتوری‌ها از بایگانی‌ها به مسیر مشخص:

`engrampa --extract-to={{path/to/directory}} {{path/to/archive1.tar path/to/archive2.tar ...}}`
