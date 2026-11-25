# uinput

> دریافت و نوشتن رویدادهای ورودی در دستگاه صفحه‌کلید مجازی با `/dev/uinput`.
> اطلاعات بیشتر: <https://gitlab.com/interception/linux/tools/-/tree/master#uinput>.

- شبیه‌سازی ادغام توضیحات دستگاه و چاپ YAML حاصل:

`uinput -p`

- ادغام توضیحات دستگاه YAML در دستگاه مجازی حاصل:

`sudo uinput -c {{path/to/device1.yaml path/to/device2.yaml ...}}`

- ادغام توضیحات دستگاه مرجع از گره‌های دستگاه در دستگاه مجازی حاصل:

`sudo uinput -d {{/dev/input/eventX /dev/input/eventY ...}}`
