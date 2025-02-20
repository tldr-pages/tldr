# cp

> کپی فایل‌ها و پوشه‌ها.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>.

- کپی یک فایل به مکان دیگر:

`cp {{path/to/source_file.ext}} {{path/to/target_file.ext}}`

- کپی یک فایل به یک پوشه دیگر با حفظ نام فایل:

`cp {{path/to/source_file.ext}} {{path/to/target_parent_directory}}`

- کپی بازگشتی محتویات یک پوشه به مکان دیگر (اگر مقصد وجود داشته باشد، پوشه داخل آن کپی می‌شود):

`cp -r {{path/to/source_directory}} {{path/to/target_directory}}`

- کپی بازگشتی یک پوشه در حالت پرگویی (فایل‌ها هنگام کپی نمایش داده می‌شوند):

`cp -vr {{path/to/source_directory}} {{path/to/target_directory}}`

- کپی چندین فایل به صورت همزمان به یک پوشه:

`cp -t {{path/to/destination_directory}} {{path/to/file1 path/to/file2 ...}}`

- کپی تمام فایل‌ها با پسوند مشخص به مکان دیگر در حالت تعاملی (قبل از رونویسی از کاربر سؤال می‌شود):

`cp -i {{*.ext}} {{path/to/target_directory}}`

- پیروی از پیوندهای نمادین قبل از کپی:

`cp -L {{link}} {{path/to/target_directory}}`

- استفاده از مسیر کامل فایل‌های مبدأ و ایجاد پوشه‌های میانی مفقود هنگام کپی:

`cp --parents {{source/path/to/file}} {{path/to/target_file}}`
