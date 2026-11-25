# lxc-create

> ایجاد کانتینرهای لینوکس.
> اطلاعات بیشتر: <https://linuxcontainers.org/lxc/getting-started/>.

- ایجاد تعاملی کانتینر در `/var/lib/lxc/`:

`sudo lxc-create {{[-n|--name]}} {{container_name}} {{[-t|--template]}} download`

- ایجاد کانتینر در دایرکتوری مقصد:

`sudo lxc-create {{[-P|--lxcpath]}} /{{path/to/directory}}/ {{[-n|--name]}} {{container_name}} {{[-t|--template]}} download`

- ایجاد کانتینر با ارسال گزینه‌ها به قالب:

`sudo lxc-create {{[-n|--name]}} {{container_name}} {{[-t|--template]}} download -- {{[-d|--dist]}} {{distro_name}} {{[-r|--release]}} {{release_version}} {{[-a|--arch]}} {{architecture}}`

- نمایش راهنما:

`lxc-create {{[-?|--help]}}`
