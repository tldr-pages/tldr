# whatis

> نمایش توضیحات یک‌خطی از صفحات راهنما.
> همچنین : `man`, `whereis`.
> اطلاعات بیشتر: <https://manned.org/whatis>.

- نمایش توضیح یک صفحهٔ راهنما:

`whatis {{command}}`

- قطع نکردن توضیح در انتهای خط:

`whatis {{[-l|--long]}} {{command}}`

- نمایش توضیحات همهٔ دستورهای مطابق با یک `glob`:

`whatis {{[-w|--wildcard]}} {{net*}}`

- جست‌وجوی توضیحات صفحات راهنما با یک `regex`:

`whatis {{[-r|--regex]}} '{{wish[0-9]\.[0-9]}}'`

- نمایش توضیحات به زبانی مشخص:

`whatis {{[-L|--locale]}} {{en}} {{command}}`
