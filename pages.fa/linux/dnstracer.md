# dnstracer

> تعیین منشأ اطلاعات یک DNS.
> اطلاعات بیشتر: <https://manned.org/dnstracer>.

- یافتن منشأ اطلاعات www.example.com در DNS محلی:

`dnstracer www.example.com`

- شروع با یک DNS مشخص و شناخته‌شده با `-s`:

`dnstracer -s {{dns.example.org}} {{www.example.com}}`

- پرس‌وجو فقط از سرورهای IPv4 با `-4`:

`dnstracer -4 {{www.example.com}}`

- تلاش مجدد هر درخواست ۵ بار در صورت شکست با `-r`:

`dnstracer -r 5 {{www.example.com}}`

- نمایش همهٔ مراحل هنگام اجرا:

`dnstracer -v {{www.example.com}}`

- نمایش نمای کلی همهٔ پاسخ‌های دریافت‌شده پس از اجرا با `-o`:

`dnstracer -o {{www.example.com}}`
