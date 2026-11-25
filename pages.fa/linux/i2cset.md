# i2cset

> تنظیم مقدار رجیستر دستگاه I2C.
> توجه: همهٔ آدرس‌ها باید به‌صورت شانزده‌شانزدهی مشخص شوند.
> همچنین : `i2cdetect`, `i2cdump`, `i2cget`.
> اطلاعات بیشتر: <https://manned.org/i2cset>.

- نوشتن در رجیستر دستگاه I2C:

`i2cset {{i2cbus}} {{device_address}} {{register_address}} {{value}}`

- نوشتن در رجیستر دستگاه I2C بدون درخواست تأیید:

`i2cset -y {{i2cbus}} {{device_address}} {{register_address}} {{value}}`

- نوشتن در رجیستر دستگاه I2C با حالت مشخص:

`i2cset {{i2cbus}} {{device_address}} {{register_address}} {{value}} {{b|w|c|s|i}}`
