# systemctl bind

> اتصال موقت فایل یا دایرکتوری میزبان به فضای نام اتصال یک واحد با bind mount.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#bind%20UNIT%20PATH%20%5BPATH%5D>.

- اتصال مسیر میزبان به همان محل داخل واحد:

`systemctl bind {{unit}} /{{path/to/host_directory}}`

- اتصال مسیر میزبان به محلی دیگر داخل واحد:

`systemctl bind {{unit}} /{{path/to/host_directory}} /{{path/to/unit_directory}}`

- اتصال مسیر به‌صورت فقط‌خواندنی داخل واحد:

`systemctl bind {{unit}} /{{path/to/host_directory}} --read-only`

- ایجاد مسیر مقصد داخل واحد پیش از اتصال:

`systemctl bind {{unit}} /{{path/to/host_directory}} /{{path/to/unit_directory}} --mkdir`
