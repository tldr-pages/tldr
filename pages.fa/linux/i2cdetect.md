# i2cdetect

> پویش گذرگاه‌های I2C.
> همچنین : `i2cdump`, `i2cget`, `i2cset`.
> اطلاعات بیشتر: <https://manned.org/i2cdetect>.

- فهرست کردن گذرگاه‌های فعال I2C:

`i2cdetect -l`

- پویش دستگاه‌ها روی گذرگاه I2C:

`i2cdetect {{i2c_bus}}`

- پویش دستگاه‌ها روی گذرگاه I2C بدون درخواست تأیید:

`i2cdetect -y {{i2c_bus}}`
