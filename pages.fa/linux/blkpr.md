# blkpr

> ثبت، رزرو، آزادسازی، جایگزینی و پاک کردن رزروهای پایدار روی یک دستگاه بلوکی که از رزرو پایدار پشتیبانی می‌کند.
> اطلاعات بیشتر: <https://manned.org/blkpr>.

- ثبت یک رزرو جدید با کلید مشخص روی یک دستگاه مشخص:

`blkpr {{[-c|--command]}} register {{[-k|--key]}} {{reservation_key}} {{path/to/device}}`

- تنظیم نوع یک رزرو موجود به دسترسی انحصاری:

`blkpr {{[-c|--command]}} reserve {{[-k|--key]}} {{reservation_key}} {{[-t|--type]}} exclusive-access {{path/to/device}}`

- جایگزینی رزرو موجود با کلید مشخص با یک رزرو جدید:

`blkpr {{[-c|--command]}} preempt {{[-K|--oldkey]}} {{old_key}} {{[-k|--key]}} {{new_key}} {{[-t|--type]}} write-exclusive {{path/to/device}}`

- آزادسازی یک رزرو با کلید و نوع مشخص روی یک دستگاه مشخص:

`blkpr {{[-c|--command]}} release {{[-k|--key]}} {{reservation_key}} {{[-t|--type]}} {{reservation_type}} {{path/to/device}}`

- پاک کردن همهٔ رزروهای یک دستگاه مشخص:

`blkpr {{[-c|--command]}} clear {{[-k|--key]}} {{key}} {{path/to/device}}`
