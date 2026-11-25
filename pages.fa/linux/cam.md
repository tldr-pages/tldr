# cam

> ابزار رابط برای `libcamera`.
> همچنین ببینید: `v4l2-ctl`.
> اطلاعات بیشتر: <https://docs.libcamera.org/>.

- فهرست کردن دوربین‌های موجود:

`cam {{[-l|--list]}}`

- فهرست کردن کنترل‌های یک دوربین:

`cam {{[-c|--camera]}} {{camera_index}} --list-controls`

- نوشتن فریم‌ها در یک پوشه:

`cam {{[-c|--camera]}} {{camera_index}} {{[-C|--capture=]}}{{frames_to_capture}} {{[-F|--file]}}`

- نمایش تصویر زندهٔ دوربین در یک پنجره:

`cam {{[-c|--camera]}} {{camera_index}} {{[-C|--capture]}} {{[-S|--sdl]}}`
