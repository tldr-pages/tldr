# tegrastats

> پایش مصرف حافظه و پردازنده برای دستگاه‌های مبتنی بر NVIDIA Jetson.
> توجه: حذف `sudo` باعث حذف بخشی از خروجی می‌شود.
> اطلاعات بیشتر: <https://developer.nvidia.com/docs/drive/drive-os/7.0.3/public/drive-os-linux-sdk/development-workflow/NVIDIA_DRIVE_Utilities/tegrastats_Utility/tegrastatsOptions32.html>.

- چاپ مکرر آمار سیستم:

`sudo tegrastats`

- تنظیم فاصلهٔ دلخواه بر حسب میلی‌ثانیه:

`sudo tegrastats --interval {{1000}}`

- نوشتن خروجی در فایل:

`sudo tegrastats --logfile {{filename}}`
