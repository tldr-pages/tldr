# sfill

> بازنویسی امن فضای آزاد و inodeهای پارتیشنی که دایرکتوری مشخص در آن قرار دارد.
> اطلاعات بیشتر: <https://manned.org/sfill>.

- بازنویسی فضای آزاد و inodeهای دیسک با ۳۸ بار نوشتن (کند اما امن):

`sfill /{{path/to/mounted_disk_directory}}`

- بازنویسی فضای آزاد و inodeهای دیسک با ۶ بار نوشتن (سریع اما کم‌امنیت‌تر) و نمایش وضعیت:

`sfill -l -v /{{path/to/mounted_disk_directory}}`

- بازنویسی فضای آزاد و inodeهای دیسک با یک بار نوشتن (بسیار سریع اما کم‌امنیت‌تر) و نمایش وضعیت:

`sfill -ll -v /{{path/to/mounted_disk_directory}}`

- بازنویسی فقط فضای آزاد دیسک:

`sfill -I /{{path/to/mounted_disk_directory}}`

- بازنویسی فقط inodeهای آزاد دیسک:

`sfill -i /{{path/to/mounted_disk_directory}}`
