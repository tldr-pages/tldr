# importctl

> بارگیری، وارد یا صادر کردن تصاویر دیسک.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/importctl.html>.

- بارگیری تصویر در قالب tarball از یک URL با pull:

`sudo importctl pull-tar {{url}} {{path/to/directory}}`

- دریافت یا بارگیری فایل خام یا `.qcow2` از منبع راه دور و ذخیره به‌صورت فایل خام:

`sudo importctl pull-raw {{https://example.com/source.ext}} {{name}} --class={{machine|portable|sysext|confext}}`

- وارد کردن تصویر دیسک خام، که احتمالاً با `xz`، `gzip` یا `bzip2` فشرده شده، به دایرکتوری تصاویر:

`importctl import-raw {{path/to/file.ext}} {{name}} --class={{machine|portable|sysext|confext}}`

- صادر کردن تصویر کانتینر به‌صورت tarball در دایرکتوری کاری فعلی:

`importctl export-tar --class={{machine|portable|sysext|confext}} {{name}} {{path/to/file.ext}}`
