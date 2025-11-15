# tar

> ابزار آرشیو کردن.
> اغلب با یک روش فشرده‌سازی مانند `gzip` یا `bzip2` ترکیب می‌شود.
> اطلاعات بیشتر: <https://www.gnu.org/software/tar/manual/tar.html>.

- [c]ایجاد یک آرشیو و نوشتن آن در یک [f]فایل:

`tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}`

- [c]ایجاد یک آرشیو g[z]ip شده و نوشتن آن در یک [f]فایل:

`tar czf {{path/to/target.tar.gz}} {{path/to/file1 path/to/file2 ...}}`

- [c]ایجاد یک آرشیو g[z]ip شده (فشرده) از یک پوشه با استفاده از مسیرهای نسبی:

`tar czf {{path/to/target.tar.gz}} {{[-C|--directory]}} {{path/to/directory}} .`

- استخراج [x] یک آرشیو (فشرده) [f]فایل در پوشه فعلی به صورت [v]کامل:

`tar xvf {{path/to/source.tar[.gz|.bz2|.xz]}}`

- استخراج [x] یک آرشیو (فشرده) [f]فایل در پوشه مقصد:

`tar xf {{path/to/source.tar[.gz|.bz2|.xz]}} {{[-C|--directory]}} {{path/to/directory}}`

- [c]ایجاد یک آرشیو فشرده و نوشتن آن در یک [f]فایل، با استفاده از پسوند فایل برای تعیین [a]خودکار برنامه فشرده‌سازی:

`tar caf {{path/to/target.tar.xz}} {{path/to/file1 path/to/file2 ...}}`

- نمایش [t] محتویات یک فایل [f]tar به صورت [v]کامل:

`tar tvf {{path/to/source.tar}}`

- استخراج [x] فایل‌های منطبق با یک الگو از یک آرشیو [f]فایل:

`tar xf {{path/to/source.tar}} --wildcards "{{*.html}}"`
