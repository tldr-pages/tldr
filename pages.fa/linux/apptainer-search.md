# apptainer search

> جست‌وجوی تصاویر کانتینر در یک کتابخانهٔ کانتینر.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_search.html>.

- جست‌وجوی تصاویر کانتینر مطابق با عبارت جست‌وجو:

`apptainer search {{query}}`

- جست‌وجوی تصاویر کانتینر برای یک معماری مشخص:

`apptainer search --arch {{amd64|arm64|386|ppc64le|s390x}} {{query}}`

- جست‌وجوی فقط تصاویر کانتینر امضاشده:

`apptainer search --signed {{query}}`

- جست‌وجو در یک کتابخانهٔ کانتینر مشخص:

`apptainer search --library {{library_url}} {{query}}`

- نمایش راهنما:

`apptainer search {{[-h|--help]}}`
