# export

> صادر کردن متغیرهای پوسته به فرایندهای فرزند.
> اطلاعات بیشتر: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- تنظیم یک متغیر محیطی:

`export {{VARIABLE}}={{value}}`

- لغو صدور یک متغیر محیطی:

`export -n {{VARIABLE}}`

- صادر کردن یک تابع به فرایندهای فرزند با `-f`:

`export -f {{FUNCTION_NAME}}`

- افزودن یک مسیر به انتهای متغیر محیطی `$PATH`:

`export PATH=$PATH:{{path/to/append}}`

- چاپ فهرست متغیرهای فعال صادرشده در قالب دستور پوسته با `-p`:

`export -p`
