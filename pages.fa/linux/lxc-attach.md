# lxc-attach

> اتصال به کانتینر.
> اطلاعات بیشتر: <https://linuxcontainers.org/lxc/getting-started/>.

- اتصال به کانتینر:

`sudo lxc-attach {{container_name}}`

- اتصال به کانتینر بدون انتقال متغیرهای محیطی میزبان به آن:

`sudo lxc-attach {{container_name}} --clear-env`

- نمایش راهنما:

`lxc-attach {{[-?|--help]}}`
