# busctl

> بازرسی و پایش گذرگاه D-Bus.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/busctl.html>.

- نمایش همهٔ همتایان روی گذرگاه بر اساس نام سرویس آن‌ها:

`busctl`

- نمایش اطلاعات فرایند و اعتبارنامه‌های یک سرویس گذرگاه، یک فرایند یا مالک گذرگاه (اگر پارامتری مشخص نشود):

`busctl status {{service|pid}}`

- چاپ پیام‌های در حال تبادل؛ اگر سرویسی مشخص نشود، همهٔ پیام‌های گذرگاه نمایش داده می‌شوند:

`busctl monitor {{service1 service2 ...}}`

- نمایش درخت اشیای یک یا چند سرویس (یا همهٔ سرویس‌ها اگر سرویسی مشخص نشود):

`busctl tree {{service1 service2 ...}}`

- نمایش رابط‌ها، متدها، ویژگی‌ها و سیگنال‌های شیء مشخص در سرویس مشخص:

`busctl introspect {{service}} {{path/to/object}}`

- دریافت مقدار فعلی یک یا چند ویژگی شیء:

`busctl get-property {{service}} {{path/to/object}} {{interface_name}} {{property_name}}`

- فراخوانی یک متد و نمایش پاسخ:

`busctl call {{service}} {{path/to/object}} {{interface_name}} {{method_name}}`
