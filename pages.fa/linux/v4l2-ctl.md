# v4l2-ctl

> کنترل دستگاه‌های ویدئویی.
> همچنین ببینید: `cam`.
> اطلاعات بیشتر: <https://manned.org/v4l2-ctl>.

- فهرست کردن همهٔ دستگاه‌های ویدئویی:

`v4l2-ctl {{[-A|--list-devices]}}`

- فهرست کردن قالب‌ها و وضوح‌های ویدئویی پشتیبانی‌شدهٔ دستگاه پیش‌فرض `/dev/video0`:

`v4l2-ctl --list-formats-ext`

- فهرست کردن قالب‌ها و وضوح‌های ویدئویی پشتیبانی‌شدهٔ دستگاه مشخص:

`v4l2-ctl --list-formats-ext {{[-d|--device]}} {{path/to/video_device}}`

- دریافت همهٔ جزئیات دستگاه ویدئویی:

`v4l2-ctl --all {{[-d|--device]}} {{path/to/video_device}}`

- گرفتن عکس JPEG با وضوح مشخص از دستگاه ویدئویی:

`v4l2-ctl {{[-d|--device]}} {{path/to/video_device}} --set-fmt-video=width={{width}},height={{height}},pixelformat=MJPG --stream-mmap --stream-to={{path/to/output.jpg}} --stream-count=1`

- ضبط جریان ویدئوی خام از دستگاه ویدئویی:

`v4l2-ctl {{[-d|--device]}} {{path/to/video_device}} --set-fmt-video=width={{width}},height={{height}},pixelformat={{format}} --stream-mmap --stream-to={{path/to/output}} --stream-count={{number_of_frames_to_capture}}`

- فهرست کردن همهٔ کنترل‌های دستگاه ویدئویی و مقادیر آن‌ها:

`v4l2-ctl {{[-l|--list-ctrls]}} {{[-d|--device]}} {{path/to/video_device}}`

- تنظیم مقدار کنترل دستگاه ویدئویی:

`v4l2-ctl {{[-d|--device]}} {{path/to/video_device}} {{[-c|--set-ctrl]}} {{control_name}}={{value}}`
