# i2cget

> خواندن از رجیستر دستگاه I2C.
> توجه: همهٔ آدرس‌ها باید به‌صورت شانزده‌شانزدهی مشخص شوند.
> همچنین : `i2cdetect`, `i2cdump`, `i2cset`.
> اطلاعات بیشتر: <https://manned.org/i2cget>.

- خواندن از رجیستر دستگاه I2C:

`i2cget {{i2cbus}} {{device_address}} {{register_address}}`

- خواندن از رجیستر دستگاه I2C بدون درخواست تأیید:

`i2cget -y {{i2cbus}} {{device_address}} {{register_address}}`

- خواندن از رجیستر دستگاه I2C با حالت مشخص:

`i2cget {{i2cbus}} {{device_address}} {{register_address}} {{b|w|c|s|i}}`
