# sqfstar

> ایجاد فایل‌سیستم squashfs از بایگانی `.tar`.
> اطلاعات بیشتر: <https://manned.org/sqfstar>.

- ایجاد فایل‌سیستم squashfs (به‌طور پیش‌فرض فشرده‌شده با `gzip`) از بایگانی `.tar` فشرده‌نشده:

`sqfstar <{{archive.tar}} {{filesystem.squashfs}}`

- ایجاد فایل‌سیستم squashfs از بایگانی `.tar` فشرده‌شده با `gzip` و فشرده‌سازی فایل‌سیستم با الگوریتم مشخص:

`zcat {{archive.tar.gz}} | sqfstar -comp {{gzip|lzo|lz4|xz|zstd|lzma}} {{filesystem.squashfs}}`

- ایجاد فایل‌سیستم squashfs از بایگانی `.tar` فشرده‌شده با `xz`، با مستثنا کردن برخی فایل‌ها:

`xzcat {{archive.tar.xz}} | sqfstar {{filesystem.squashfs}} {{file1 file2 ...}}`

- ایجاد فایل‌سیستم squashfs از بایگانی `.tar` فشرده‌شده با `zstd`، با مستثنا کردن فایل‌های منتهی به `.gz`:

`zstdcat {{archive.tar.zst}} | sqfstar {{filesystem.squashfs}} "{{*.gz}}"`

- ایجاد فایل‌سیستم squashfs از بایگانی `.tar` فشرده‌شده با `lz4`، با مستثنا کردن فایل‌های مطابق `regex`:

`lz4cat {{archive.tar.lz4}} | sqfstar {{filesystem.squashfs}} -regex "{{regex}}"`
