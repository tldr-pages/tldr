# swaplabel

> چاپ یا تغییر برچسب یا UUID فضای swap.
> توجه: `path/to/file` می‌تواند به فایل معمولی یا پارتیشن swap اشاره کند.
> اطلاعات بیشتر: <https://manned.org/swaplabel>.

- نمایش برچسب و UUID فعلی فضای swap:

`swaplabel {{path/to/file}}`

- تنظیم برچسب فضای swap:

`swaplabel {{[-L|--label]}} {{new_label}} {{path/to/file}}`

- تنظیم UUID فضای swap (می‌توانید UUID را با `uuidgen` تولید کنید):

`swaplabel {{[-U|--uuid]}} {{new_uuid}} {{path/to/file}}`
