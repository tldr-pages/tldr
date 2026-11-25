# lxc-ls

> فهرست کردن کانتینرهای لینوکس.
> اطلاعات بیشتر: <https://linuxcontainers.org/lxc/manpages/man1/lxc-ls.1.html>.

- فهرست کردن همهٔ کانتینرها:

`sudo lxc-ls`

- فهرست کردن کانتینرهای فعال (شامل منجمد و در حال اجرا):

`sudo lxc-ls --active`

- فهرست کردن فقط کانتینرهای منجمد:

`sudo lxc-ls --frozen`

- فهرست کردن فقط کانتینرهای متوقف‌شده:

`sudo lxc-ls --stopped`

- فهرست کردن کانتینرها در خروجی ستونی و زیبا:

`sudo lxc-ls {{[-f|--fancy]}}`

- نمایش راهنما:

`lxc-ls {{[-?|--help]}}`
