# stress

> آزمون فشار CPU، حافظه و ورودی/خروجی در سیستم لینوکس.
> اطلاعات بیشتر: <https://manned.org/stress>.

- ایجاد ۴ worker برای آزمون فشار CPU:

`stress {{[-c|--cpu]}} 4`

- ایجاد ۲ worker برای آزمون فشار ورودی/خروجی و پایان پس از ۵ ثانیه:

`stress {{[-i|--io]}} 2 {{[-t|--timeout]}} 5`

- ایجاد ۲ worker برای آزمون فشار حافظه (هر worker مقدار 256M بایت تخصیص می‌دهد):

`stress {{[-m|--vm]}} 2 --vm-bytes 256M`

- ایجاد ۲ worker در حلقهٔ write()/unlink() (هر worker مقدار 1G بایت می‌نویسد):

`stress {{[-d|--hdd]}} 2 --hdd-bytes 1GB`
