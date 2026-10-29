# gst-launch-1.0 vulkanh264enc

> Encode video into h264 using the Vulkan API.
> More information: <https://gstreamer.freedesktop.org/documentation/vulkan/vulkanh264enc.html>.

- Encode h264 video:

`gst-launch-1.0 {{source}} ! vulkanupload ! vulkanh264enc ! h264parse ! {{sink}}`
