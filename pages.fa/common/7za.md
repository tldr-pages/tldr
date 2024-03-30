# 7za

> آرشیو کننده فایل با قدرت فشرده سازی بالا.
> عملکرد مشابه `7z` بااین تفاوت که دستور مزبور از نوع فایل کمتری پشتیبانی می کند اما چند-سکویی است.
> اطلاعات بیشتر: <https://manned.org/7za>.

- آرشیو یک فایل یا پوشه:

`7za a {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- رمزنگاری یک آرشیو موجود (شامل نام فایلها):

`7za a {{path/to/encrypted.7z}} -p{{password}} -mhe={{on}} {{path/to/archive.7z}}`

- استخراج یک آرشیو درحالی که ساختار پوشه اصلی حفظ می شود:

`7za x {{path/to/archive.7z}}`

- استخراج یک آرشیو در پوشه موردنظر:

`7za x {{path/to/archive.7z}} -o{{path/to/output}}`

- استخراج یک آرشیو در `stdout`:

`7za x {{path/to/archive.7z}} -so`

- آرشیو کردن با نوع آرشیو دلخواه:

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- فهرست کردن محتواهای یک آرشیو:

`7za l {{path/to/archive.7z}}`

- تنظیم میزان فشرده سازی (مقادیر بیشتر به معنی فشرده سازی بیشتر اما آهسته تر است):

`7za a {{path/to/archive.7z}} -mx={{0|1|3|5|7|9}} {{path/to/file_or_directory}}`
