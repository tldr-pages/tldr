# hyprshot

> ابزار تصویربرداری از صفحه برای ترکیب‌گر Wayland به نام Hyprland.
> اطلاعات بیشتر: <https://github.com/Gustash/Hyprshot>.

- انتخاب یک ناحیه و گرفتن تصویر آن:

`hyprshot {{[-m|--mode]}} region`

- انتخاب پنجرهٔ مشخص و گرفتن تصویر آن:

`hyprshot {{[-m|--mode]}} window`

- انتخاب خروجی مشخص و گرفتن تصویر آن:

`hyprshot {{[-m|--mode]}} output`

- گرفتن تصویر پنجرهٔ فعال فعلی:

`hyprshot {{[-m|--mode]}} active {{[-m|--mode]}} window`

- ثابت کردن صفحه و گرفتن تصویر ناحیهٔ انتخاب‌شده:

`hyprshot {{[-z|--freeze]}} {{[-m|--mode]}} region`

- انتخاب پنجرهٔ مشخص، گرفتن تصویر و ذخیره در دایرکتوری خروجی مشخص:

`hyprshot {{[-o|--output-folder]}} {{path/to/directory}} {{[-m|--mode]}} window`

- انتخاب خروجی مشخص و گرفتن تصویر آن فقط در کلیپ‌بورد:

`hyprshot --clipboard {{[-m|--mode]}} output`
