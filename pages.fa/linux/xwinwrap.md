# xwinwrap

> اجرای پخش‌کننده یا برنامه به‌عنوان پس‌زمینهٔ دسکتاپ.
> اطلاعات بیشتر: <https://github.com/r00tdaemon/xwinwrap>.

- اجرای ویدئو با mpv:

`xwinwrap -b -nf -ov -- {{mpv}} --wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{path/to/video.mp4}}`

- اجرای ویدئو به‌صورت تمام‌صفحه با mpv:

`xwinwrap -b -nf -fs -ov -- {{mpv}} --wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{path/to/video.mp4}}`

- اجرای ویدئو با mpv و کدری ۸۰٪:

`xwinwrap -b -nf -ov -o 0.8 --- {{mpv}} --wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{path/to/video.mp4}}`

- اجرای ویدئو با mpv در نمایشگر دوم با اندازهٔ 1600x900 و جابه‌جایی ۱۹۲۰ روی محور X:

`xwinwrap -g 1600x900+1920 -b -nf -ov -- {{mpv}} --wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{path/to/video.mkv}}`
