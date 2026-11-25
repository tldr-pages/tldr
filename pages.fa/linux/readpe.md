# readpe

> نمایش اطلاعات فایل‌های PE.
> اطلاعات بیشتر: <https://manned.org/readpe>.

- نمایش همهٔ اطلاعات فایل PE:

`readpe {{path/to/executable}}`

- نمایش همهٔ سربرگ‌های موجود در فایل PE:

`readpe --all-headers {{path/to/executable}}`

- نمایش همهٔ بخش‌های موجود در فایل PE:

`readpe --all-sections {{path/to/executable}}`

- نمایش سربرگ مشخص از فایل PE:

`readpe --header {{dos|coff|optional}} {{path/to/executable}}`

- فهرست کردن همهٔ توابع واردشده:

`readpe --imports {{path/to/executable}}`

- فهرست کردن همهٔ توابع صادرشده:

`readpe --exports {{path/to/executable}}`
