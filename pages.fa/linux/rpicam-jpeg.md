# rpicam-jpeg

> گرفتن و ذخیرهٔ تصویر JPEG با دوربین Raspberry Pi.
> اطلاعات بیشتر: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-jpeg>.

- گرفتن تصویر و نام‌گذاری فایل:

`rpicam-jpeg {{[-o|--output]}} {{path/to/file.jpg}}`

- گرفتن تصویر با ابعاد تعیین‌شده:

`rpicam-jpeg {{[-o|--output]}} {{path/to/file.jpg}} --width {{1920}} --height {{1080}}`

- گرفتن تصویر با نوردهی ۲۰ میلی‌ثانیه و بهرهٔ ۱۵۰٪:

`rpicam-jpeg {{[-o|--output]}} {{path/to/file.jpg}} --shutter 20000 --gain 1.5`
