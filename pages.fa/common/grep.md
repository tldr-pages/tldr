# grep

> یافتن الگو در فایل ها به کمک عبارات با قاعده.
> اطلاعات بیشتر: <https://www.gnu.org/software/grep/manual/grep.html>.

- جستجو یک الگو در یک فایل :

`grep "{{search_pattern}}" {{path/to/file}}`

- جستجو یک عبارت خاص (معادل مقایسه رشته ای) :

`grep {{[-F|--fixed-strings]}} "{{exact_string}}" {{path/to/file}}`

- جستجو بازگشتی یک الگو در تمامی فایل های یک پوشه، نمایش تمامی خطوط منطبق، فایل های باینری را رد میکند:

`grep {{[-rnI|--recursive --line-number --binary-files=without-match]}} "{{search_pattern}}" {{path/to/directory}}`

- استفاده از عبارات با قاعده توسعه یافته (با پشتیبانی از `?`، `+`، `{}`، `()`، و `|`)، در حالت حساس به بزرگی کوچکی کاراکتر ها :

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{search_pattern}}" {{path/to/file}}`

- چاپ 3 خط از قبل و بعد محل انطباق:

`grep {{--context|--before-context|--after-context}} 3 "{{search_pattern}}" {{path/to/file}}`

- چاپ نام فایل و شماره خط برای هر انطباق با رنگبندی :

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{search_pattern}}" {{path/to/file}}`

- جستجوی خطوط منطبق، چاپ متن منطبق :

`grep {{[-o|--only-matching]}} "{{search_pattern}}" {{path/to/file}}`

- ورودی استاندارد (`stdin`) رو برای الگوهایی که منطبق نیستند جستجو میکند :

`cat {{path/to/file}} | grep {{[-v|--invert-match]}} "{{search_pattern}}"`
