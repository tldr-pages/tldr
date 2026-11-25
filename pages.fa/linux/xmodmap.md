# xmodmap

> ابزار تغییر نگاشت کلیدها و دکمه‌های اشاره‌گر در X.
> اطلاعات بیشتر: <https://manned.org/xmodmap>.

- جابه‌جایی کلیک چپ `<LeftClick>` و کلیک راست `<RightClick>` اشاره‌گر:

`xmodmap -e 'pointer = 3 2 1'`

- تخصیص مجدد کلید صفحه‌کلید به کلیدی دیگر:

`xmodmap -e 'keycode {{keycode}} = {{keyname}}'`

- غیرفعال کردن کلید صفحه‌کلید:

`xmodmap -e 'keycode {{keycode}} ='`

- اجرای همهٔ عبارت‌های xmodmap در فایل مشخص:

`xmodmap {{path/to/file}}`
