# apx stacks

> مدیریت پشته‌ها در `apx`.
> توجه: پیکربندی‌های پشته که توسط کاربر ساخته شده‌اند در `~/.local/share/apx/stacks` ذخیره می‌شوند.
> اطلاعات بیشتر: <https://docs.vanillaos.org/docs/en/apx-manpage#stacks>.

- ساخت تعاملی یک پیکربندی پشتهٔ جدید:

`apx stacks new`

- به‌روزرسانی تعاملی یک پیکربندی پشته:

`apx stacks update {{name}}`

- فهرست کردن همهٔ پیکربندی‌های موجود پشته:

`apx stacks list`

- حذف یک پیکربندی پشتهٔ مشخص:

`apx stacks rm --name {{string}}`

- وارد کردن یک پیکربندی پشته:

`apx stacks import --input {{path/to/stack.yml}}`

- صادر کردن پیکربندی پشته (توجه: گزینهٔ خروجی اختیاری است و به‌صورت پیش‌فرض در دایرکتوری کاری فعلی صادر می‌شود):

`apx stacks export --name {{string}} --output {{path/to/output_file}}`
