# dpkg-deb

> بسته‌بندی، باز کردن و ارائهٔ اطلاعات دربارهٔ بایگانی‌های دبیان.
> اطلاعات بیشتر: <https://manned.org/dpkg-deb>.

- نمایش اطلاعات یک بسته:

`dpkg-deb {{[-I|--info]}} {{path/to/file.deb}}`

- نمایش نام و نسخهٔ بسته در یک خط:

`dpkg-deb {{[-W|--show]}} {{path/to/file.deb}}`

- فهرست کردن محتویات بسته:

`dpkg-deb {{[-c|--contents]}} {{path/to/file.deb}}`

- استخراج محتویات بسته در یک دایرکتوری:

`dpkg-deb {{[-x|--extract]}} {{path/to/file.deb}} {{path/to/directory}}`

- ایجاد بسته از دایرکتوری مشخص:

`dpkg-deb {{[-b|--build]}} {{path/to/directory}}`
