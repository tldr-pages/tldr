# flameshot

> ابزار تصویربرداری از صفحه با رابط گرافیکی.
> از ویرایش پایهٔ تصویر مانند متن، شکل‌ها، رنگ‌ها و imgur پشتیبانی می‌کند.
> اطلاعات بیشتر: <https://flameshot.org/docs/advanced/commandline-options/>.

- ایجاد تصویر از کل صفحه:

`flameshot full`

- ایجاد تعاملی تصویر صفحه:

`flameshot gui`

- ایجاد تصویر صفحه و ذخیره در مسیر مشخص:

`flameshot gui {{[-p|--path]}} {{path/to/directory}}`

- ایجاد تعاملی تصویر صفحه در حالت ساده‌شده:

`flameshot launcher`

- ایجاد تصویر صفحه از یک نمایشگر مشخص:

`flameshot screen {{[-n|--number]}} {{2}}`

- ایجاد تصویر صفحه و چاپ آن در خروجی استاندارد `stdout`:

`flameshot gui {{[-r|--raw]}}`

- ایجاد تصویر صفحه و کپی آن در کلیپ‌بورد:

`flameshot gui {{[-c|--clipboard]}}`

- ایجاد تصویر صفحه با تأخیر مشخص بر حسب میلی‌ثانیه:

`flameshot full {{[-d|--delay]}} {{5000}}`
