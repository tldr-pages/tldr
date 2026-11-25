# bluetoothctl

> مدیریت دستگاه‌های بلوتوث.
> همچنین ببینید: `bluetui`.
> اطلاعات بیشتر: <https://manned.org/bluetoothctl>.

- ورود به پوستهٔ تعاملی `bluetoothctl`:

`bluetoothctl`

- فهرست کردن همهٔ دستگاه‌های شناخته‌شده:

`bluetoothctl devices`

- روشن یا خاموش کردن کنترل‌کنندهٔ بلوتوث:

`bluetoothctl power {{on|off}}`

- پویش دستگاه‌های موجود به مدت ۱۰ ثانیه:

`bluetoothctl {{[-t|--timeout]}} 10 scan on`

- جفت شدن با یک دستگاه:

`bluetoothctl pair {{mac_address}}`

- اتصال به یک دستگاه جفت‌شده یا قطع اتصال از آن:

`bluetoothctl {{connect|disconnect}} {{mac_address}}`

- اجازه دادن به دستگاه برای اتصال مجدد:

`bluetoothctl trust {{mac_address}}`

- حذف یک دستگاه:

`bluetoothctl remove {{mac_address}}`
