# v4l2-ctl

> 控制视频设备。
> 更多信息：<https://manned.org/v4l2-ctl>。

- 列出所有视频设备：

`v4l2-ctl --list-devices`

- 列出默认视频设备 `/dev/video0` 支持的视频格式和分辨率：

`v4l2-ctl --list-formats-ext`

- 列出特定视频设备支持的视频格式和分辨率：

`v4l2-ctl --list-formats-ext --device {{path/to/video_device}}`

- 获取视频设备的所有详细信息：

`v4l2-ctl --all --device {{path/to/video_device}}`

- 从视频设备捕获具有特定分辨率的 JPEG 照片：

`v4l2-ctl --device {{path/to/video_device}} --set-fmt-video=width={{width}},height={{height}},pixelformat=MJPG --stream-mmap --stream-to={{path/to/output.jpg}} --stream-count=1`

- 从视频设备捕获原始视频流：

`v4l2-ctl --device {{path/to/video_device}} --set-fmt-video=width={{width}},height={{height}},pixelformat={{format}} --stream-mmap --stream-to={{path/to/output}} --stream-count={{number_of_frames_to_capture}}`

- 列出所有视频设备的控制项及其值：

`v4l2-ctl --list-ctrls --device {{path/to/video_device}}`

- 设置视频设备控制项的值：

`v4l2-ctl --device {{path/to/video_device}} --set-ctrl={{control_name}}={{value}}`