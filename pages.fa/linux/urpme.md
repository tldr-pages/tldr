# urpme

> حذف نصب بسته‌ها در Mageia.
> همچنین ببینید: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> اطلاعات بیشتر: <https://man.linuxreviews.org/man8/urpme.8.html>.

- حذف نصب بسته:

`sudo urpme {{package}}`

- حذف نصب بسته‌های یتیم (توجه: با احتیاط استفاده کنید زیرا ممکن است بسته‌های مهم را ناخواسته حذف کند):

`sudo urpme --auto-orphans`

- حذف نصب بسته و وابستگی‌های آن:

`sudo urpme --auto-orphans {{package}}`
