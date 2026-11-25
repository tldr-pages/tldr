# gpu-screen-recorder

> ضبط صفحه و رمزگذاری ویدئو با پردازندهٔ گرافیکی.
> اطلاعات بیشتر: <https://git.dec05eba.com/gpu-screen-recorder/about/>.

- انتخاب منبع با پورتال میزکار و ضبط آن:

`gpu-screen-recorder -w portal -o {{path/to/video.mp4}}`

- تعیین منبع ویدئوی مشخص:

`gpu-screen-recorder -w {{screen|DP-1|HDMI-A1|...}} -o {{path/to/video.mp4}}`

- فهرست کردن منابع تصویربرداری:

`gpu-screen-recorder --list-capture-options`

- فهرست کردن منابع ضبط صدا:

`gpu-screen-recorder {{--list-audio-devices|--list-application-audio}}`

- ضبط با استفاده از بافر بازپخش:

`gpu-screen-recorder -w {{screen}} -r {{30}} -c {{mp4}} -ro {{path/to/directory}} -o {{whatever}}`

- گرفتن ویدئو از بافر بازپخش:

`pkill {{[-USR1|-SIGUSR1]}} -f gpu-screen-recorder`

- اجرای `gpu-screen-recorder` در پس‌زمینه:

`systemctl start --user gpu-screen-recorder`
