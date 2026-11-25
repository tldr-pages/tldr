# modprobe

> افزودن یا حذف ماژول‌ها از هستهٔ لینوکس.
> همچنین : `lsmod`, `kmod`.
> اطلاعات بیشتر: <https://manned.org/modprobe>.

- شبیه‌سازی بارگذاری ماژول در هسته:

`modprobe {{[-n|--dry-run]}} {{module_name}}`

- بارگذاری ماژول در هسته:

`sudo modprobe {{module_name}}`

- بارگذاری چند ماژول:

`sudo modprobe {{[-a|--all]}} {{module_name1 module_name2 ...}}`

- حذف ماژول از هسته:

`sudo modprobe {{[-r|--remove]}} {{module_name}}`

- حذف ماژول و ماژول‌های وابسته به آن از هسته:

`sudo modprobe {{[-r|--remove]}} --remove-holders {{module_name}}`

- نمایش وابستگی‌های ماژول هسته:

`sudo modprobe {{[-D|--show-depends]}} {{module_name}}`
