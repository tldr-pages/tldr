# instaloader

> بارگیری تصاویر، ویدئوها، زیرنویس‌ها و سایر فراداده‌ها از Instagram.
> توجه: برای بارگیری رسانه با کیفیت بالا باید اطلاعات ورود Instagram را ارائه کنید.
> اطلاعات بیشتر: <https://instaloader.github.io/cli-options.html>.

- بارگیری یک پروفایل:

`instaloader {{profile_name}}`

- بارگیری هایلایت‌ها:

`instaloader --highlights {{profile_name}}`

- بارگیری پست‌های دارای برچسب مکانی (در صورت وجود)، بدون تعامل با کاربر:

`instaloader {{[-q|--quiet]}} {{[-G|--geotags]}} {{profile_name}}`

- تعیین عامل کاربر برای درخواست‌های HTTP:

`instaloader --user-agent {{user_agent}} {{profile_name}}`

- تعیین اطلاعات ورود و بارگیری پست‌ها (مفید برای پروفایل‌های خصوصی):

`instaloader {{[-l|--login]}} {{username}} {{[-p|--password]}} {{password}} {{profile_name}}`

- رد کردن هدف در صورت یافتن نخستین فایل بارگیری‌شده (مفید برای به‌روزرسانی بایگانی‌های Instagram):

`instaloader {{[-F|--fast-update]}} {{profile_name}}`

- بارگیری استوری‌ها و ویدئوهای IGTV (نیازمند ورود):

`instaloader {{[-l|--login]}} {{username}} {{[-p|--password]}} {{password}} {{[-s|--stories]}} --igtv {{profile_name}}`

- بارگیری همهٔ انواع پست‌ها (نیازمند ورود):

`instaloader {{[-l|--login]}} {{username}} {{[-p|--password]}} {{password}} {{[-s|--stories]}} --igtv --highlights {{profile_name}}`
