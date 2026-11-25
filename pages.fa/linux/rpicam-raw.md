# rpicam-raw

> ضبط ویدئوی خام با دوربین Raspberry Pi.
> اطلاعات بیشتر: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-raw>.

- ضبط ویدئو برای تعداد ثانیهٔ مشخص:

`rpicam-raw {{[-t|--timeout]}} {{2000}} {{[-o|--output]}} {{path/to/file.raw}}`

- تغییر ابعاد و نرخ فریم ویدئو:

`rpicam-raw {{[-t|--timeout]}} {{5000}} --width {{4056}} --height {{3040}} {{[-o|--output]}} {{path/to/file.raw}} --framerate {{8}}`
