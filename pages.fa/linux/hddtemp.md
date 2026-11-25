# hddtemp

> نمایش دمای HDD از طریق S.M.A.R.T.
> اطلاعات بیشتر: <https://manned.org/hddtemp>.

- نمایش دمای درایو مشخص:

`hddtemp {{type}}:{{/dev/sdX}}`

- نمایش دمای درایو SATA اختصاص‌یافته به `sda`:

`hddtemp SATA:/dev/sda`

- ثبت دما در syslog هر `n` ثانیه:

`hddtemp {{[-S|--syslog]}} {{nseconds}} {{type}}:{{/dev/sdX}}`

- چاپ فقط مقدار عددی دما بدون واحد:

`hddtemp {{[-n|--numeric]}} {{type}}:{{/dev/sdX}}`

- تعیین واحد نمایش دما:

`hddtemp {{[-u|--unit]}} {{C|F}} {{type}}:{{/dev/sdX}}`

- بیدار کردن درایو ATA پیش از تلاش برای خواندن دما:

`hddtemp {{[-w|--wake-up]}} {{type}}:{{/dev/sdX}}`

- ورود به حالت اشکال‌زدایی برای نمایش فیلدهای S.M.A.R.T. و مقادیر آن‌ها:

`hddtemp {{[-D|--debug]}} {{type}}:{{/dev/sdX}}`

- صرف‌نظر از بررسی سازگاری انواع درایو:

`hddtemp {{[-q|--quiet]}} {{type}}:{{/dev/sdX}}`
