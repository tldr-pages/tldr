# tod

> کارخواه کوچک Todoist نوشته‌شده با Rust.
> ورودی ساده را دریافت و در صندوق ورودی یا پروژهٔ دیگر ذخیره می‌کند و از پردازش زبان طبیعی برای تعیین موعد، برچسب‌ها و غیره بهره می‌برد.
> اطلاعات بیشتر: <https://github.com/tod-org/tod/blob/main/docs/usage.md#usage>.

- وارد کردن پروژه‌ها (برای فعال کردن پرسش پروژه ضروری است):

`tod project import`

- ایجاد سریع وظیفه با موعد:

`tod --quickadd {{Buy more milk today}}`

- ایجاد وظیفهٔ جدید (محتوا و پروژه پرسیده می‌شوند):

`tod task create`

- ایجاد وظیفه در پروژه:

`tod task create --content "{{Write more rust}}" --project {{code}}`

- دریافت وظیفهٔ بعدی پروژه:

`tod task next`

- دریافت برنامهٔ کاری:

`tod task list --scheduled --project {{work}}`

- دریافت همهٔ وظایف کاری:

`tod task list --project {{work}}`
