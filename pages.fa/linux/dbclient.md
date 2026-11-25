# dbclient

> کارخواه سبک پوستهٔ امن Dropbear.
> اطلاعات بیشتر: <https://manned.org/dbclient>.

- اتصال به یک میزبان راه دور:

`dbclient {{user}}@{{host}}`

- اتصال به یک میزبان راه دور روی درگاه ۲۲۲۲ با `-p`:

`dbclient {{user}}@{{host}} -p 2222`

- اتصال به میزبان راه دور با کلید هویت مشخص در قالب dropbear با `-i`:

`dbclient -i {{path/to/key_file}} {{user}}@{{host}}`

- اجرای یک دستور روی میزبان راه دور با تخصیص tty توسط `-t` برای امکان تعامل با دستور راه دور:

`dbclient {{user}}@{{host}} -t {{command}} {{argument1 argument2 ...}}`

- اتصال و انتقال اتصال‌های عامل احراز هویت به میزبان راه دور با `-A`:

`dbclient -A {{user}}@{{host}}`
