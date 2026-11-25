# add-apt-repository

> مدیریت تعریف مخازن `apt`.
> اطلاعات بیشتر: <https://manned.org/add-apt-repository>.

- افزودن یک مخزن جدید `apt`:

`add-apt-repository {{repository_spec}}`

- حذف یک مخزن `apt`:

`add-apt-repository {{[-r|--remove]}} {{repository_spec}}`

- به‌روزرسانی حافظهٔ نهان بسته‌ها پس از افزودن مخزن:

`add-apt-repository --update {{repository_spec}}`

- اجازه دادن به دانلود بسته‌های منبع از مخزن:

`add-apt-repository {{[-s|--enable-source]}} {{repository_spec}}`
