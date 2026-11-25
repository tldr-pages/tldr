# mksquashfs

> ایجاد یا افزودن فایل‌ها و دایرکتوری‌ها به فایل‌سیستم‌های squashfs.
> اطلاعات بیشتر: <https://manned.org/mksquashfs>.

- ایجاد یا افزودن فایل‌ها و دایرکتوری‌ها به فایل‌سیستم squashfs (به‌طور پیش‌فرض با `gzip` فشرده می‌شود):

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}}`

- ایجاد یا افزودن فایل‌ها و دایرکتوری‌ها به فایل‌سیستم squashfs با الگوریتم فشرده‌سازی مشخص:

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}} -comp {{gzip|lzo|lz4|xz|zstd|lzma}}`

- ایجاد یا افزودن فایل‌ها و دایرکتوری‌ها به فایل‌سیستم squashfs با مستثنا کردن برخی از آن‌ها:

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}} -e {{file|directory1 file|directory2 ...}}`

- ایجاد یا افزودن فایل‌ها و دایرکتوری‌ها به فایل‌سیستم squashfs با مستثنا کردن موارد منتهی به `gzip`:

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}} -wildcards -e "{{*.gz}}"`

- ایجاد یا افزودن فایل‌ها و دایرکتوری‌ها به فایل‌سیستم squashfs با مستثنا کردن موارد مطابق `regex`:

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}} -regex -e "{{regex}}"`
