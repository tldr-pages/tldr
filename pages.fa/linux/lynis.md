# lynis

> ابزار ممیزی سیستم و امنیت.
> اطلاعات بیشتر: <https://cisofy.com/documentation/lynis/>.

- بررسی به‌روز بودن Lynis:

`sudo lynis update info`

- اجرای ممیزی امنیتی سیستم:

`sudo lynis audit system`

- اجرای ممیزی امنیتی Dockerfile:

`sudo lynis audit dockerfile {{path/to/dockerfile}}`
