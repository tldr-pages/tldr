# i2cdump

> I2C 장치의 레지스터 내용을 출력.
> 관련 항목: `i2cdetect`, `i2cget`, `i2cset`.
> 참고: All addresses should be specified in hexadecimal.
> 더 많은 정보: <https://manned.org/i2cdump>.

- I2C 장치의 모든 레지스터 내용 출력:

`i2cdump {{i2cbus}} {{장치_주소}}`

- 확인 메시지 없이 I2C 장치의 모든 레지스터 내용 출력:

`i2cdump -y {{i2cbus}} {{장치_주소}}`

- 지정한 모드로 I2C 장치의 모든 레지스터 내용 출력:

`i2cdump {{i2cbus}} {{장치_주소}} {{b|w|c|s|i}}`

- I2C 장치의 지정한 범위(`start` ~ `end`)의 레지스터 내용을 출력:

`i2cdump -r {{시작}}-{{끝}} {{i2cbus}} {{장치_주소}}`
