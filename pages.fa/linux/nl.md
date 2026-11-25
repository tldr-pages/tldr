# nl

> شماره‌گذاری خط‌های فایل یا ورودی `stdin`.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/nl-invocation.html>.

- شماره‌گذاری خط‌های غیرخالی فایل:

`nl {{path/to/file}}`

- خواندن از `stdin`:

`{{command}} | nl`

- شماره‌گذاری همهٔ خط‌های بدنه از جمله خط‌های خالی یا شماره‌گذاری نکردن خط‌های بدنه:

`nl {{[-b|--body-numbering]}} {{a|n}} {{path/to/file}}`

- شماره‌گذاری فقط خط‌های بدنهٔ مطابق الگوی `regex` پایه (BRE):

`nl {{[-b|--body-numbering]}} p'FooBar[0-9]' {{path/to/file}}`

- استفاده از گام مشخص برای شماره‌گذاری خط‌ها:

`nl {{[-i|--line-increment]}} {{increment}} {{path/to/file}}`

- تعیین قالب شماره‌گذاری خط‌ها به‌صورت راست‌چین یا چپ‌چین با حفظ صفرهای ابتدایی یا بدون آن‌ها:

`nl {{[-n|--number-format]}} {{rz|ln|rn}}`

- تعیین عرض شماره‌گذاری خط‌ها (پیش‌فرض ۶):

`nl {{[-w|--number-width]}} {{col_width}} {{path/to/file}}`

- استفاده از رشتهٔ مشخص برای جدا کردن شمارهٔ خط‌ها از متن آن‌ها (پیش‌فرض `TAB`):

`nl {{[-s|--number-separator]}} {{separator}} {{path/to/file}}`
