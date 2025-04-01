# fswebcam

> 用于 *nix 系统的小巧简单的网络摄像头工具。
> 更多信息：<https://www.sanslogic.co.uk/fswebcam>。

- 拍摄照片：

`fswebcam {{filename}}`

- 使用自定义分辨率拍摄照片：

`fswebcam -r {{width}}x{{height}} {{filename}}`

- 从选定的设备拍摄照片（默认设备为 `/dev/video0`）：

`fswebcam -d {{device}} {{filename}}`

- 带时间戳拍摄照片（时间戳字符串由 strftime 格式化）：

`fswebcam --timestamp {{timestamp}} {{filename}}`
