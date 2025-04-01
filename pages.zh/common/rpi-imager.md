# rpi-imager

> 将镜像写入存储设备。
> 更多信息：<https://github.com/raspberrypi/rpi-imager>.

- 将特定的镜像写入特定的块设备：

`rpi-imager --cli {{path/to/image.zip}} {{/dev/sdX}}`

- 将特定的镜像写入块设备，禁用校验和验证：

`rpi-imager --cli --disable-verify {{path/to/image.zip}} {{/dev/sdX}}`

- 将特定的镜像写入块设备，并在验证时期望特定的校验和：

`rpi-imager --cli --sha256 {{expected_hash}} {{path/to/image.zip}} {{/dev/sdX}}`