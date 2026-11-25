# rpicam-still

> گرفتن و ذخیرهٔ عکس با دوربین Raspberry Pi، همراه با قابلیت‌های قدیمی که در `rpicam-jpeg` وجود ندارند.
> اطلاعات بیشتر: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-still>.

- گرفتن عکس با رمزگذاری متفاوت:

`rpicam-still {{[-e|--encoding]}} {{bmp|png|rgb|yuv420}} {{[-o|--output]}} {{path/to/file.ext}}`

- گرفتن تصویر خام:

`rpicam-still {{[-r|--raw]}} {{[-o|--output]}} {{path/to/file.jpg}}`

- گرفتن تصویر با نوردهی ۱۰۰ میلی‌ثانیه:

`rpicam-still {{[-o|--output]}} {{path/to/file.jpg}} --shutter 100000`
