# rpi-imager

> Flash képek tárolóeszközökre való felvitele. További információ: <https://github.com/raspberrypi/rpi-imager>.

- Egy adott kép írása egy adott blokkeszközre:

`rpi-imager --cli {{path/to/image.zip}} {{/dev/sdX}}`

- Egy adott kép írása egy blokkeszközre, az ellenőrzőösszeg-ellenőrzés letiltásával:

`rpi-imager --cli --disable-verify {{path/to/image.zip}} {{/dev/sdX}}`

- Írjon egy adott képet egy blokkeszközre, amely az ellenőrzés futtatásakor egy adott ellenőrző összeget vár el:

`rpi-imager --cli --sha256 {{expected_hash}} {{path/to/image.zip}} {{/dev/sdX}}`
