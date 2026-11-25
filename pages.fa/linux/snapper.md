# snapper

> ابزار مدیریت snapshot فایل‌سیستم.
> اطلاعات بیشتر: <http://snapper.io/manpages/snapper.html>.

- فهرست کردن پیکربندی‌های snapshot:

`snapper list-configs`

- ایجاد پیکربندی snapper:

`snapper {{[-c|--config]}} {{config}} create-config {{path/to/directory}}`

- ایجاد snapshot همراه با توضیح:

`snapper {{[-c|--config]}} {{config}} create {{[-d|--description]}} "{{snapshot_description}}"`

- فهرست کردن snapshotهای پیکربندی:

`snapper {{[-c|--config]}} {{config}} list`

- حذف snapshot:

`snapper {{[-c|--config]}} {{config}} delete {{snapshot_number}}`

- حذف بازه‌ای از snapshotها:

`snapper {{[-c|--config]}} {{config}} delete {{snapshot1}}-{{snapshot2}}`
