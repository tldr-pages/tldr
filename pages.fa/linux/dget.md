# dget

> دانلود بسته‌های دبیان.
> اطلاعات بیشتر: <https://manned.org/dget>.

- دانلود یک بستهٔ دودویی:

`dget {{package}}`

- دانلود و استخراج منبع یک بسته از فایل `.dsc` آن:

`dget {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`

- دانلود بایگانی tar منبع یک بسته از فایل `.dsc` آن بدون استخراج:

`dget {{[-d|--download-only]}} {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`
