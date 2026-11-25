# slurp

> انتخاب ناحیه‌ای در ترکیب‌گر Wayland.
> اطلاعات بیشتر: <https://github.com/emersion/slurp/blob/master/slurp.1.scd>.

- انتخاب ناحیه و چاپ آن در `stdout`:

`slurp`

- انتخاب ناحیه و چاپ آن در `stdout` همراه با نمایش ابعاد انتخاب:

`slurp -d`

- انتخاب یک نقطه به‌جای ناحیه:

`slurp -p`

- انتخاب خروجی و چاپ نام آن:

`slurp -o -f '%o'`

- انتخاب ناحیهٔ مشخص و گرفتن تصویر بدون حاشیه با `grim`:

`grim -g "$(slurp -w 0)"`

- انتخاب ناحیهٔ مشخص و گرفتن ویدئوی بدون حاشیه با `wf-recorder`:

`wf-recorder {{[-g|--geometry]}} "$(slurp -w 0)"`
