# 7zr

> آرشیو کننده فایل با قدرت فشرده سازی بالا.
> عملکردی مشابه `7z` با این تفاوت که از فایلهای `.7z` پشتیبانی نمی کند.
> اطلاعات بیشتر: <https://manned.org/7zr>.

- آرشیو کردن یک فایل یا پوشه:

`7zr a {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- رمزنگاری آرشیو موجود (همراه با اسم فایلها):

`7zr a {{path/to/encrypted.7z}} -p{{password}} -mhe={{on}} {{path/to/archive.7z}}`

- استخراج یک آرشیو درحالی که ساختار پوشه اصلی حفظ می شود:

`7zr x {{path/to/archive.7z}}`

- استخراج یک آرشیو در پوشه مورد نظر:

`7zr x {{path/to/archive.7z}} -o{{path/to/output}}`

- استخراج یک آرشیو در `stdout`:

`7zr x {{path/to/archive.7z}} -so`

- فهرست کردن محتواهای یک آرشیو:

`7zr l {{path/to/archive.7z}}`

- تنظیم میزان فشرده سازی (مقادیر بیشتر به معنی فشرده سازی بیشتر اما آهسته تر است):

`7zr a {{path/to/archive.7z}} -mx={{0|1|3|5|7|9}} {{path/to/file_or_directory}}`
