# fbset

> نمایش و تغییر تنظیمات دستگاه بافر فریم.
> اطلاعات بیشتر: <https://manned.org/fbset.1>.

- نمایش تنظیمات فعلی بافر فریم:

`sudo fbset {{[-i|--info]}}`

- تنظیم حالت بافر فریم تعریف‌شده در `/etc/fb.modes`:

`sudo fbset "{{800}}x{{600}}-{{60}}"`

- تنظیم ابعاد بافر فریم:

`sudo fbset -xres {{horizontal_pixels}} -yres {{vertical_pixels}}`

- تنظیم حالت دلخواه بافر فریم:

`sudo fbset {{[-g|--geometry]}} {{tty_horizontal}} {{tty_vertical}} {{monitor_horizontal}} {{monitor_vertical}} {{color_depth}}`
