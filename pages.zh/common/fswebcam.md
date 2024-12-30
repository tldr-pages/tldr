# fswebcam

> 小而简单的网络摄像头程序，适用于 *nix。
> 更多信息：<https://www.sanslogic.co.uk/fswebcam>。

- 拍摄一张照片：

`fswebcam {{filename}}`

- 以自定义分辨率拍摄一张照片：

`fswebcam -r {{width}}x{{height}} {{filename}}`

- 从选定设备拍摄一张照片（默认是 `/dev/video0`）：

`fswebcam -d {{device}} {{filename}}`

- 拍摄一张带时间戳的照片（时间戳字符串格式由 strftime 定义）：

`fswebcam --timestamp {{timestamp}} {{filename}}`