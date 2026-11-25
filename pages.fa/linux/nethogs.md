# nethogs

> پایش مصرف پهنای باند به تفکیک فرایند.
> اطلاعات بیشتر: <https://manned.org/nethogs>.

- شروع NetHogs با دسترسی root (دستگاه پیش‌فرض `eth0` است):

`sudo nethogs`

- پایش پهنای باند دستگاه مشخص:

`sudo nethogs {{device}}`

- پایش پهنای باند چند دستگاه:

`sudo nethogs {{device1 device2 ...}}`

- تعیین فاصلهٔ تازه‌سازی بر حسب ثانیه:

`sudo nethogs -d {{seconds}}`

- تغییر واحد نمایش ترافیک (پیش‌فرض: ۰؛ ۰ = kB/s، ۱ = کل kB، ۲ = کل بایت، ۳ = کل MB، ۴ = MB/s، ۵ = GB/s):

`sudo nethogs -v {{0..5}}`
