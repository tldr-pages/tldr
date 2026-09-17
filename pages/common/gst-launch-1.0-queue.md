# gst-launch-1.0 queue

> Multithread the pipeline and buffer data.
> More information: <https://gstreamer.freedesktop.org/documentation/coreelements/queue.html>.

- Separate a pipeline into multiple threads so that one blocking element doesn't block the rest:

`gst-launch-1.0 {{source}} ! queue ! {{sink}}`
