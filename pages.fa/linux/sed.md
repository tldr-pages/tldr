# sed

> ویرایشگر جریان GNU برای فیلتر و تبدیل متن.
> همچنین : `awk`, `ed`.
> اطلاعات بیشتر: <https://www.gnu.org/software/sed/manual/sed.html>.

- جایگزینی همهٔ موارد «apple» با «mango» در همهٔ خط‌ها و چاپ در `stdout`:

`{{command}} | sed 's/apple/mango/g'`

- جایگزینی «apple» با «mango» درجا در فایل (بازنویسی فایل اصلی):

`sed {{[-i|--in-place]}} 's/apple/mango/g' {{path/to/file}}`

- اجرای چند جایگزینی در یک دستور:

`{{command}} | sed -e '{{s/apple/mango/g}}' -e '{{s/orange/lime/g}}'`

- استفاده از جداکنندهٔ دلخواه (هنگامی که الگو حاوی اسلش است مفید است):

`{{command}} | sed '{{s#////#____#g}}'`

- حذف خط‌های ۱ تا ۵ فایل و پشتیبان‌گیری از فایل اصلی با پسوند `.orig`:

`sed {{[-i|--in-place=]}}.orig '1,5d' {{path/to/file}}`

- چاپ فقط خط نخست در `stdout`:

`{{command}} | sed {{[-n|--quiet]}} '1p'`

- درج خط جدید در ابتدای فایل و بازنویسی فایل اصلی:

`sed {{[-i|--in-place]}} '1i\your new line text\' {{path/to/file}}`

- حذف خط‌های خالی (با یا بدون فاصله یا tab) از فایل و بازنویسی فایل اصلی:

`sed {{[-i|--in-place]}} '/^[[:space:]]*$/d' {{path/to/file}}`
