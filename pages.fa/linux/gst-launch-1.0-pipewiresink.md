# gst-launch-1.0 pipewiresink

> ایجاد یک گره PipeWire برای خروجی دادن داده از آن.
> اطلاعات بیشتر: <https://github.com/PipeWire/pipewire/tree/master/src/gst>.

- خروجی دادن ویدئوی آزمایشی:

`gst-launch-1.0 videotestsrc ! pipewiresink mode=provide`

- نام‌گذاری گره PipeWire:

`gst-launch-1.0 {{videotestsrc}} ! pipewiresink mode=provide client-name={{node_name}}`
