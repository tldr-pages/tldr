# imv

> نمایشگر تصویر خط فرمان برای Wayland و X11، مخصوص مدیران پنجرهٔ کاشی‌وار.
> از قالب‌های متعدد از جمله Photoshop (PSD) پشتیبانی می‌کند.
> اطلاعات بیشتر: <https://sr.ht/~exec64/imv/>.

- مشاهدهٔ چند تصویر:

`imv {{path/to/image1.ext path/to/image2.ext ...}}`

- مشاهده در حالت تمام‌صفحه:

`imv -f {{path/to/image.ext}}`

- مشاهدهٔ بازگشتی تصاویر از یک مسیر:

`imv -r --slideshow {{path/to/directory}}`

- باز کردن چند تصویر از طریق `stdin`:

`find . -type f -name "{{*.svg}}" | imv`

- ساخت نمایش اسلاید از یک دایرکتوری با نمایش هر تصویر به مدت ۱۰ ثانیه:

`imv -t 10 {{path/to/directory}}`

- مشاهدهٔ چند تصویر از وب:

`curl {{[-Osw|--remote-name --silent --write-out]}} '%{filename_effective}\n' '{{http://www.example.com/[1-10].jpg}}' | imv`
