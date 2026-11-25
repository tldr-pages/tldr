# ebuild

> رابط سطح پایین برای سامانهٔ Portage در جنتو.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Ebuild>.

- ایجاد یا به‌روزرسانی مانیفست بسته:

`ebuild {{path/to/file.ebuild}} manifest`

- پاکسازی دایرکتوری‌های ساخت موقت برای فایل ساخت:

`ebuild {{path/to/file.ebuild}} clean`

- دریافت منابع در صورت موجود نبودن:

`ebuild {{path/to/file.ebuild}} fetch`

- استخراج منابع در دایرکتوری ساخت موقت:

`ebuild {{path/to/file.ebuild}} unpack`

- کامپایل منابع استخراج‌شده:

`ebuild {{path/to/file.ebuild}} compile`

- نصب بسته در دایرکتوری نصب موقت:

`ebuild {{path/to/file.ebuild}} install`

- نصب فایل‌های موقت در سیستم فایل فعال:

`ebuild {{path/to/file.ebuild}} qmerge`

- دریافت، استخراج، کامپایل، نصب و اجرای qmerge برای فایل ebuild مشخص:

`ebuild {{path/to/file.ebuild}} merge`
