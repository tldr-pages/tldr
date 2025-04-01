# gst-launch-1.0

> 构建并运行 GStreamer 管道。
> 更多信息：<https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html?gi-language=c>.

- 在窗口中播放测试视频：

`gst-launch-1.0 videotestsrc ! xvimagesink`

- 在窗口中播放媒体文件：

`gst-launch-1.0 playbin uri={{protocol}}://{{host}}/{{path/to/file}}`

- 重新编码媒体文件：

`gst-launch-1.0 filesrc location={{path/to/file}} ! {{file_type}}demux ! {{codec_type}}dec ! {{codec_type}}enc ! {{file_type}}mux ! filesink location={{path/to/file}}`

- 将文件流式传输到 RTSP 服务器：

`gst-launch-1.0 filesrc location={{path/to/file}} ! rtspclientsink location=rtsp://{{host_IP}}/{{path/to/file}}`
