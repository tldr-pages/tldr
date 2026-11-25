# gst-launch-1.0 pipewiresrc

> خواندن داده از یک گره PipeWire.
> اطلاعات بیشتر: <https://github.com/PipeWire/pipewire/tree/master/src/gst>.

- گوش دادن به میکروفون پیش‌فرض:

`gst-launch-1.0 pipewiresrc ! autoaudiosink`

- تعیین گره برای ضبط و مشاهدهٔ ویدئو در پنجره:

`gst-launch-1.0 pipewiresrc target-object={{node_name}} ! autovideosink`

- ضبط ویدئو در فایل:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc ! videoconvert ! {{x264enc}} ! {{h264parse}} ! {{matroskamux}} ! filesink location={{path/to/file.mkv}}`

- گرفتن تصویر صفحه از گره ویدئو:

`gst-launch-1.0 pipewiresrc num-buffers=1 ! videoconvert ! {{pngenc}} ! filesink location={{path/to/file.png}}`

- ضبط صدا در فایل:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc ! {{opusenc}} ! {{oggmux}} ! filesink location={{path/to/file.ogg}}`

- ضبط خروجی پایش یک دستگاه:

`gst-launch-1.0 pipewiresrc target-object={{node_name}} stream-properties=props,stream.capture.sink=true ! {{audioconvert ! fakesink}}`

- ترکیب صدا و ویدئو در یک فایل:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc do-timestamp=true ! videoconvert ! {{x264enc}} ! {{h264parse}} ! {{mux}}. pipewiresrc do-timestamp=true ! {{opusenc}} ! {{mux}}. {{matroskamux}} name={{mux}} ! filesink location={{path/to/file.mkv}}`
