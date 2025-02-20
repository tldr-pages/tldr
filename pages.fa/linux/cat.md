# cat

> نمایش و ترکیب محتوای فایل‌ها.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>.

- نمایش محتوای یک فایل در `stdout`:

`cat {{path/to/file}}`

- ترکیب چندین فایل و ذخیره در یک فایل خروجی:

`cat {{path/to/file1 path/to/file2 ...}} > {{path/to/output_file}}`

- اضافه کردن محتوای چند فایل به انتهای یک فایل خروجی:

`cat {{path/to/file1 path/to/file2 ...}} >> {{path/to/output_file}}`

- نوشتن ورودی استاندارد (`stdin`) در یک فایل:

`cat - > {{path/to/file}}`

- نمایش شماره خط برای تمام خطوط خروجی:

`cat -n {{path/to/file}}`

- نمایش کاراکترهای غیرقابل چاپ و فضای خالی (با پیشوند `M-` برای کاراکترهای غیر ASCII):

`cat -v -t -e {{path/to/file}}`
