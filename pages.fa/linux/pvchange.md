# pvchange

> تغییر ویژگی‌های حجم‌های فیزیکی.
> اطلاعات بیشتر: <https://manned.org/pvchange>.

- مجاز کردن تخصیص در حجم فیزیکی:

`sudo pvchange {{[-x|--allocatable]}} y {{/dev/sdXN}}`

- غیرمجاز کردن تخصیص در حجم فیزیکی:

`sudo pvchange {{[-x|--allocatable]}} n {{/dev/sdXN}}`

- نادیده گرفتن ناحیه‌های فراداده در حجم فیزیکی:

`sudo pvchange --metadataignore y {{/dev/sdXN}}`

- توقف نادیده گرفتن ناحیه‌های فراداده در حجم فیزیکی:

`sudo pvchange --metadataignore n {{/dev/sdXN}}`

- افزودن برچسب به حجم فیزیکی:

`sudo pvchange --addtag {{tag}} {{/dev/sdXN}}`

- تولید UUID جدید برای حجم فیزیکی (با احتیاط استفاده کنید):

`sudo pvchange --uuid {{/dev/sdXN}}`

- تغییر همهٔ حجم‌های فیزیکی قابل مشاهده (با گزینه‌های دیگر مانند قابلیت تخصیص ترکیب کنید):

`sudo pvchange {{[-a|--all]}} {{[-x|--allocatable]}} y`
