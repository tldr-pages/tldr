# dconf

> مدیریت پایگاه‌های دادهٔ dconf.
> همچنین : `gsettings`.
> اطلاعات بیشتر: <https://manned.org/dconf>.

- چاپ مقدار یک کلید مشخص:

`dconf read /{{path/to/key}}`

- چاپ زیرشاخه‌ها و زیرکلیدهای یک مسیر مشخص:

`dconf list /{{path/to/directory}}/`

- نوشتن مقدار یک کلید مشخص:

`dconf write /{{path/to/key}} "{{value}}"`

- بازنشانی مقدار یک کلید مشخص:

`dconf reset /{{path/to/key}}`

- پایش تغییرات یک کلید یا دایرکتوری مشخص:

`dconf watch /{{path/to/key|/path/to/directory}}/`

- چاپ محتویات یک دایرکتوری مشخص در قالب فایل INI:

`dconf dump /{{path/to/directory}}/`
