# paccache

> ابزار پاک‌سازی حافظهٔ نهان `pacman`.
> اطلاعات بیشتر: <https://manned.org/paccache>.

- حذف همهٔ نسخه‌های بسته‌ها به‌جز ۳ نسخهٔ جدیدتر از حافظهٔ نهان `pacman`:

`paccache {{[-r|--remove]}}`

- تعیین تعداد نسخه‌های بسته برای نگهداری:

`paccache {{[-rk|--remove --keep]}} {{num_versions}}`

- شبیه‌سازی پاک‌سازی و نمایش تعداد بسته‌های نامزد حذف:

`paccache {{[-d|--dryrun]}}`

- انتقال بسته‌های نامزد به دایرکتوری به‌جای حذف آن‌ها:

`paccache {{[-m|--move]}} {{path/to/directory}}`
