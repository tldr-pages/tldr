# bun

> یک runtime و toolkit برای جاوا اسکریپت.
> شامل یک bundler، یک ابزار تست و یک package manager.
> اطلاعات بیشتر: <https://bun.com/docs>.

- ایجاد یک پروژه جدید Bun در دایرکتوری فعلی:

`bun init`

- اجرای یک فایل جاوااسکریپت یا یک اسکریپت در `package.json`:

`bun run {{path/to/file|script_name}}`

- اجرای تست‌های واحد:

`bun test`

- دانلود و نصب تمام بسته‌های ذکرشده در `package.json`:

`bun {{[i|install]}}`

- افزودن یک وابستگی به `package.json`:

`bun {{[a|add]}} {{module_name}}`

- حذف یک وابستگی از `package.json`:

`bun {{[rm|remove]}} {{module_name}}`

- شروع یک REPL (پوسته تعاملی):

`bun repl`

- ارتقا Bun به آخرین نسخه موجود:

`bun upgrade`
