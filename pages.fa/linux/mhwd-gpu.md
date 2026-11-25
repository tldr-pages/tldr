# mhwd-gpu

> پیکربندی کارت‌های گرافیک در Manjaro.
> اطلاعات بیشتر: <https://wiki.manjaro.org/index.php/Configure_NVIDIA_(non-free)_settings_and_load_them_on_Startup/en#Configure_The_Resolution.2FRefresh_Rate>.

- نمایش مسیر پیکربندی فعلی Xorg:

`mhwd-gpu --status`

- بررسی وجود پیوند نمادین معتبر در پیکربندی Xorg:

`mhwd-gpu --check`

- تنظیم پیکربندی دلخواه Xorg برای GPU شرکت Nvidia:

`sudo mhwd-gpu --setmod nvidia --setxorg /{{path/to/nvidia.conf}}`

- تنظیم پیکربندی دلخواه Xorg برای GPU شرکت AMD:

`sudo mhwd-gpu --setmod {{catalyst|ati}} --setxorg /{{path/to/amdgpu.conf}}`

- نمایش راهنما:

`mhwd-gpu --help`
