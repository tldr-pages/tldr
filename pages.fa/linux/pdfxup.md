# pdfxup

> چیدن چند صفحهٔ PDF در یک صفحه.
> چیدمان N-up یعنی قرار دادن چند صفحه در یک صفحه با تغییر مقیاس و چرخاندن آن‌ها در شبکه.
> اطلاعات بیشتر: <https://ctan.org/pkg/pdfxup>.

- ایجاد PDF با دو صفحه در هر صفحه:

`pdfxup {{[-o|--output]}} {{path/to/output.pdf}} {{path/to/input.pdf}}`

- ایجاد PDF با ۳ ستون و ۲ ردیف در هر صفحه:

`pdfxup {{[-x|--columns]}} 3 {{[-y|--rows]}} 2 {{[-o|--output]}} {{path/to/output.pdf}} {{path/to/input.pdf}}`

- ایجاد PDF در حالت کتابچه (دو صفحه در هر صفحه و مرتب‌شده برای تشکیل کتاب پس از تا کردن):

`pdfxup {{[-b|--booklet]}} {{[-o|--output]}} {{path/to/output.pdf}} {{path/to/input.pdf}}`
