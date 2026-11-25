# toolbox create

> ایجاد کانتینر جدید Toolbx.
> اطلاعات بیشتر: <https://manned.org/toolbox-create>.

- ایجاد کانتینر Toolbx برای توزیع مشخص:

`toolbox create {{[-d|--distro]}} {{distribution}}`

- ایجاد کانتینر Toolbx برای انتشار مشخص توزیع فعلی:

`toolbox create {{[-r|--release]}} {{release}}`

- ایجاد کانتینر Toolbx با تصویر دلخواه:

`toolbox create {{[-i|--image]}} {{name}}`

- ایجاد کانتینر Toolbx از تصویر دلخواه Fedora:

`toolbox create {{[-i|--image]}} {{quay.io/fedora/fedora:tag}}`

- ایجاد کانتینر Toolbx با تصویر پیش‌فرض انتشار مشخص Fedora:

`toolbox create {{[-d|--distro]}} {{fedora}} {{[-r|--release]}} f{{version}}`
