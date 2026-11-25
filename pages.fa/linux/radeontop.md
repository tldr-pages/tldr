# radeontop

> نمایش میزان استفاده از GPUهای AMD.
> بسته به سیستم ممکن است به دسترسی root نیاز باشد.
> همچنین ببینید: `nvtop`, `amdgpu_top`.
> اطلاعات بیشتر: <https://github.com/clbr/radeontop/blob/master/radeontop.asc>.

- نمایش میزان استفاده از GPU پیش‌فرض AMD:

`radeontop`

- فعال کردن خروجی رنگی:

`radeontop {{[-c|--color]}}`

- انتخاب GPU مشخص (شمارهٔ گذرگاه نخستین عدد در خروجی `lspci` است):

`radeontop {{[-b|--bus]}} {{bus_number}}`

- تعیین نرخ تازه‌سازی نمایش (مقدار بیشتر به معنی سربار بیشتر GPU است):

`radeontop {{[-t|--ticks]}} {{samples_per_second}}`
