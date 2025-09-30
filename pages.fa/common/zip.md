# zip

> بسته‌بندی و فشرده‌سازی (آرشیو) فایل‌ها در یک آرشیو Zip.
> همچنین ببینید: `unzip`.
> اطلاعات بیشتر: <https://manned.org/zip>.

- افزودن فایل‌ها/پوشه‌ها به یک آرشیو مشخص (به صورت بازگشتی):

`zip {{[-r|--recurse-paths]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- حذف فایل‌ها/پوشه‌ها از یک آرشیو مشخص:

`zip {{[-d|--delete]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- آرشیو فایل‌ها/پوشه‌ها با مستثنی کردن موارد مشخص شده:

`zip {{[-r|--recurse-paths]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{[-x|--exclude]}} {{path/to/excluded_files_or_directories}}`

- آرشیو فایل‌ها/پوشه‌ها با سطح فشرده‌سازی مشخص (`0` - کمترین، `9` - بیشترین):

`zip {{[-r|--recurse-paths]}} -{{0..9}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- ایجاد یک آرشیو رمزگذاری شده با رمز عبور مشخص:

`zip {{[-re|--recurse-paths --encrypt]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- آرشیو فایل‌ها/پوشه‌ها در یک آرشیو چند بخشی تقسیم شده (مثلاً بخش‌های ۳ گیگابایتی):

`zip {{[-rs|--recurse-paths --split-size]}} {{3g}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- نمایش محتویات یک آرشیو مشخص:

`zip {{[-sf|--split-size --freshen]}} {{path/to/compressed.zip}}`
