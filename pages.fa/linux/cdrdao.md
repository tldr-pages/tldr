# cdrdao

> خواندن و نوشتن CD در حالت نوشتن کل دیسک به‌صورت یک‌جا (disc-at-once).
> اطلاعات بیشتر: <https://manned.org/cdrdao>.

- خواندن یک CD و نوشتن محتویات آن در یک فایل:

`cdrdao read-cd --device {{/dev/cdrom}} --read-raw {{image.toc}}`
