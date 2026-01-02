# bun

> یک runtime و toolkit برای جاوا اسکریپت.
> شامل یک bundler، یک ابزار تست و یک package manager.
> اطلاعات بیشتر: <https://bun.com/docs>.

- اجرای یک فایل جاوااسکریپت یا یک اسکریپت در `package.json`:

`bun run {{path/to/file|script_name}}`

- اجرای تست‌های واحد:

`bun test`

- دانلود و نصب تمام بسته‌های ذکرشده در `package.json`:

`bun install`

- افزودن یک وابستگی به `package.json`:

`bun add {{module_name}}`

- حذف یک وابستگی از `package.json`:

`bun remove {{module_name}}`

- ایجاد یک پروژه جدید Bun در دایرکتوری فعلی:

`bun init`

- شروع یک REPL (پوسته تعاملی):

`bun repl`

- ارتقا Bun به آخرین نسخه موجود:

`bun upgrade`
