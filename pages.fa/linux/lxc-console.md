# lxc-console

> اتصال به کانتینر.
> اطلاعات بیشتر: <https://linuxcontainers.org/lxc/manpages//man1/lxc-console.1.html>.

- شروع کنسول در کانتینر:

`agetty {{[-L|--local-line]}} {{38400}} tty1`

- اتصال به کنسول lxc:

`sudo lxc-console {{container_name}}`

- خروج از `lxc-console`:

`<Ctrl a><q>`

- نمایش راهنما:

`lxc-console {{[-?|--help]}}`
