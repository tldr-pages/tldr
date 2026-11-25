# i2cdump

> چاپ رجیسترهای دستگاه I2C.
> توجه: همهٔ آدرس‌ها باید به‌صورت شانزده‌شانزدهی مشخص شوند.
> همچنین : `i2cdetect`, `i2cget`, `i2cset`.
> اطلاعات بیشتر: <https://manned.org/i2cdump>.

- چاپ همهٔ رجیسترهای دستگاه I2C:

`i2cdump {{i2cbus}} {{device_address}}`

- چاپ همهٔ رجیسترهای دستگاه I2C بدون درخواست تأیید:

`i2cdump -y {{i2cbus}} {{device_address}}`

- چاپ همهٔ رجیسترهای دستگاه I2C با حالت مشخص:

`i2cdump {{i2cbus}} {{device_address}} {{b|w|c|s|i}}`

- چاپ رجیسترهای دستگاه I2C از `start` تا `end`:

`i2cdump -r {{start}}-{{end}} {{i2cbus}} {{device_address}}`
