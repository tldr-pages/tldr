# runlim

> نمونه‌برداری و محدود کردن مصرف زمان و حافظهٔ برنامه و فرایندهای فرزند آن با استفاده از فایل‌سیستم proc در لینوکس.
> اطلاعات بیشتر: <https://fmv.jku.at/runlim/>.

- چاپ مصرف زمان و حافظهٔ دستور:

`runlim {{command}} {{command_arguments}}`

- ثبت آمار در فایل به‌جای `stdout`:

`runlim --output-file={{path/to/file}} {{command}} {{command_arguments}}`

- محدود کردن زمان به سقف مشخص (بر حسب ثانیه):

`runlim --time-limit={{number}} {{command}} {{command_arguments}}`

- محدود کردن زمان واقعی به سقف مشخص (بر حسب ثانیه):

`runlim --real-time-limit={{number}} {{command}} {{command_arguments}}`

- محدود کردن فضا به سقف مشخص (بر حسب MB):

`runlim --space-limit={{number}} {{command}} {{command_arguments}}`
