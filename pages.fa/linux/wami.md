# wami

> ابزار متن‌باز و آسان برای توصیهٔ برنامه‌های مناسب وظایف.
> اطلاعات بیشتر: <https://github.com/evait-security/wami>.

- یافتن نتایج گسترده در همهٔ دسته‌های lake و مرتب‌سازی آن‌ها به ترتیب مشخص:

`wami {{[-a|--show-all]}} {{[-S|--sort]}} {{asc|desc}} {{[-s|--search-all]}} {{search_string}}`

- جست‌وجوی GitHub برای یافتن نتایج گسترده، مرتب‌شده به ترتیب نزولی:

`wami {{[-a|--show-all]}} {{[-S|--sort]}} desc --github {{search_string}}`

- جست‌وجوی GitHub برای موضوعات مطابق رشتهٔ جست‌وجو:

`wami --list-topics {{search_string}}`

- جست‌وجوی lake برای ابزاری جهت پرس‌وجوی اطلاعات ورود پیش‌فرض در آزمون نفوذ و مرتب‌سازی نتایج به ترتیب نزولی:

`wami {{[-S|--sort]}} desc {{[-s|--search-all]}} pentest credential default`
