# apk

> ابزار مدیریت بسته آلپاین لینوکس.
> اطلاعات بیشتر: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- آپدیت فهرست مخزن ها از تمام مخازن ریموت:

`apk update`

- نصب یک بسته جدید:

`apk add {{package}}`

- حذف یک بسته:

`apk del {{package}}`

- تعمیر یک بسته یا ارتقا آن بدون تغییر دادن وابستگی های اصلی:

`apk fix {{package}}`

- جستجوی یک بسته با کلمات کلیدی:

`apk search {{keywords}}`

- نمایش اطلاعات درمورد بسته مورد نظر:

`apk info {{package}}`
