# toolbox run

> اجرای دستور در کانتینر موجود Toolbx.
> همچنین : `toolbox enter`.
> اطلاعات بیشتر: <https://manned.org/toolbox-run>.

- اجرای دستور داخل کانتینر مشخص Toolbx:

`toolbox run {{[-c|--container]}} {{container_name}} {{command}}`

- اجرای دستور داخل کانتینر Toolbx برای انتشار مشخص توزیع:

`toolbox run {{[-d|--distro]}} {{distribution}} {{[-r|--release]}} {{release}} {{command}}`

- اجرای `emacs` داخل کانتینر Toolbx با تصویر پیش‌فرض انتشار مشخص Fedora:

`toolbox run {{[-d|--distro]}} {{fedora}} {{[-r|--release]}} f{{version}} {{emacs}}`
