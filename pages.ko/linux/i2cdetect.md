# i2cdetect

> I2C 버스를 스캔.
> 관련 항목: `i2cdump`, `i2cget`, `i2cset`.
> 더 많은 정보: <https://manned.org/i2cdetect>.

- 활성 I2C 버스 목록 표시:

`i2cdetect -l`

- I2C 버스에 연결된 장치 스캔:

`i2cdetect {{i2c_버스}}`

- 확인 메시지 없이 I2C 버스에 연결된 장치 스캔:

`i2cdetect -y {{i2c_버스}}`
