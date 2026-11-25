# column

> قالب‌بندی ورودی استاندارد `stdin` یا یک فایل در چند ستون.
> ستون‌ها پیش از سطرها پر می‌شوند؛ جداکنندهٔ پیش‌فرض فضای خالی است.
> اطلاعات بیشتر: <https://manned.org/column>.

- قالب‌بندی خروجی یک دستور برای نمایشگری با عرض ۳۰ نویسه:

`printf "header1 header2\nbar foo\n" | column {{[-c|--output-width]}} 30`

- تقسیم خودکار ستون‌ها و تراز خودکار آن‌ها در قالب جدول:

`printf "header1 header2\nbar foo\n" | column {{[-t|--table]}}`

- تعیین نویسهٔ جداکنندهٔ ستون برای گزینهٔ `--table` (برای مثال «,» برای CSV؛ پیش‌فرض فضای خالی است):

`printf "header1,header2\nbar,foo\n" | column {{[-t|--table]}} {{[-s|--separator]}} {{,}}`

- پر کردن سطرها پیش از ستون‌ها:

`printf "header1\nbar\nfoobar\n" | column {{[-c|--output-width]}} {{30}} {{[-x|--fillrows]}}`
