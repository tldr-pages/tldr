# curlie

> رابطی برای `curl` که سهولت استفادهٔ `httpie` را اضافه می‌کند.
> اطلاعات بیشتر: <https://github.com/rs/curlie#usage>.

- ارسال یک درخواست GET:

`curlie {{httpbin.org/get}}`

- ارسال یک درخواست POST:

`curlie post {{httpbin.org/post}} {{name=john}} {{age:=25}}`

- ارسال درخواست GET با پارامترهای پرس‌وجو (مانند `first_param=5&second_param=true`):

`curlie get {{httpbin.org/get}} {{first_param==5}} {{second_param==true}}`

- ارسال درخواست GET با سربرگ دلخواه:

`curlie get {{httpbin.org/get}} {{header-name:header-value}}`
